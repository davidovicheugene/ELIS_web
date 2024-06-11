from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib import messages
from .models import *


class TodoHomepage(ListView):
    template_name = "todo_homepage.html"
    model = TodoSpace
    context_object_name = "todo_spaces"

    def get_context_data(self, **kwargs):
        context = super(TodoHomepage, self).get_context_data()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')
        context['page_title'] = 'Списки задач | Сервисы ELIS'
        context['service_name'] = 'Списки задач'
        context['space_tables'] = TodoTable.objects.filter(user=context['user'])
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TodoHomepage, self).get_queryset(*args, **kwargs)
        qs = qs.filter(user=self.request.user)
        return qs


# SPACE
class TodoAddSpace(CreateView):
    model = TodoSpace
    template_name = "todo_add_space.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('todo_homepage')  # Change url to space details view

    def get_context_data(self, **kwargs):
        context = super(TodoAddSpace, self).get_context_data()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')
        context['page_title'] = 'Создать пространство | Списки задач ELIS'
        context['service_name'] = 'Создать пространство | Списки задач'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Пространство было успешно создано!")
        return super(TodoAddSpace, self).form_valid(form)


def delete_space(request, space_id):
    space = TodoSpace.objects.get(pk=space_id)
    space.delete()
    return HttpResponseRedirect(reverse('todo_homepage'))


# TABLE
class TodoAddTable(CreateView):
    model = TodoTable
    template_name = "todo_add_table.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('todo_homepage')  # Change url to space details view

    def get_context_data(self, **kwargs):
        context = super(TodoAddTable, self).get_context_data()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')

        context['page_title'] = 'Создать доску | Списки задач ELIS'
        context['service_name'] = 'Создать доску | Списки задач'
        return context

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        form.instance.related_space = TodoSpace.objects.get(pk=self.kwargs['related_space_id'])

        form.instance.related_space.tables_count = form.instance.related_space.tables_count + 1
        form.instance.related_space.save()

        messages.success(self.request, "Доска была успешно создана!")
        return super(TodoAddTable, self).form_valid(form)


class TodoTableDetail(DetailView):
    model = TodoTable
    template_name = "todo_table_detail.html"
    context_object_name = "table"

    def get_context_data(self, **kwargs):
        context = super(TodoTableDetail, self).get_context_data()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')

        context['page_title'] = f'{context['table'].title} | {context['table'].related_space.title} | Списки задач ELIS'
        context['service_name'] = f'{context['table'].title} | Списки задач'
        context['lists'] = TodoList.objects.filter(related_table=context['table'])
        context['tasks'] = TodoTask.objects.filter(related_table=context['table'])
        return context


def delete_table(request, pk):
    table = TodoTable.objects.get(pk=pk)
    table.delete()
    return HttpResponseRedirect(reverse('todo_homepage'))


# LIST
class TodoAddList(CreateView):
    model = TodoList
    template_name = "todo_add_list.html"
    fields = ['title']
    success_url = reverse_lazy('todo_table_info')  # Change url to space details view

    def get_context_data(self, **kwargs):
        context = super(TodoAddList, self).get_context_data()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')

        context['page_title'] = 'Создать список | Списки задач ELIS'
        context['service_name'] = 'Создать список | Списки задач'
        return context

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        form.instance.related_table = TodoTable.objects.get(pk=self.kwargs['pk'])

        form.instance.related_table.lists_count = form.instance.related_table.lists_count + 1
        form.instance.related_table.save()

        messages.success(self.request, "Список был успешен создан!")
        return super(TodoAddList, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('todo_table_info', kwargs={'pk': self.object.related_table.pk})


# TASK
class TodoAddTask(CreateView):
    model = TodoTask
    template_name = "todo_add_list.html"
    fields = ['title']
    success_url = reverse_lazy('todo_table_info')  # Change url to space details view

    def get_context_data(self, **kwargs):
        context = super(TodoAddTask, self).get_context_data()
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')

        context['page_title'] = 'Создать задачу | Списки задач ELIS'
        context['service_name'] = 'Создать задачу | Списки задач'
        return context

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        form.instance.related_list = TodoList.objects.get(pk=self.kwargs['pk'])
        form.instance.related_table = TodoTable.objects.get(pk=form.instance.related_list.related_table.pk)

        form.instance.related_list.tasks_count = form.instance.related_list.tasks_count + 1
        form.instance.related_table.save()

        messages.success(self.request, "Задача была успешно создана!")
        return super(TodoAddTask, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('todo_table_info', kwargs={'pk': self.object.related_table.pk})
