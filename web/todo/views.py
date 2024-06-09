from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
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


class TodoAddSpace(CreateView):
    model = TodoSpace
    template_name = "todo_add_space.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('todo_homepage')  # Change url to space details view

    def get_context_data(self, **kwargs):
        context = super(TodoAddSpace, self).get_context_data()
        context['page_title'] = 'Создать пространство | Списки задач ELIS'
        context['service_name'] = 'Создать пространство | Списки задач'
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Пространство было успешно создано!")
        return super(TodoAddSpace, self).form_valid(form)


class TodoAddTable(CreateView):
    model = TodoTable
    template_name = "todo_add_table.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('todo_homepage')  # Change url to space details view

    def get_context_data(self, **kwargs):
        context = super(TodoAddTable, self).get_context_data()
        context['page_title'] = 'Создать доску | Списки задач ELIS'
        context['service_name'] = 'Создать доску | Списки задач'
        if self.request.user.is_authenticated:
            context['user'] = self.request.user
        else:
            reverse('user_login')
        return context

    def form_valid(self, form, **kwargs):
        form.instance.user = self.request.user
        form.instance.related_space = TodoSpace.objects.get(pk=self.kwargs['related_space_id'])

        form.instance.related_space.tables_count = form.instance.related_space.tables_count + 1
        form.instance.related_space.save()

        messages.success(self.request, "Доска была успешно создана!")
        return super(TodoAddTable, self).form_valid(form)

