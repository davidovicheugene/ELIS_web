from django.shortcuts import render
from django.views.generic import TemplateView


class TodoHomepage(TemplateView):
    template_name = "todo_homepage.html"

    def get_context_data(self, **kwargs):
        context = super(TodoHomepage, self).get_context_data()
        context['page_title'] = 'Списки задач | Сервисы ELIS'
        context['service_name'] = 'Списки задач'
        return context
