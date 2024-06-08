from django.shortcuts import render
from django.views.generic import TemplateView


class AssistanceHomepage(TemplateView):
    template_name = "index_assistance.html"

    def get_context_data(self, **kwargs):
        context = super(AssistanceHomepage, self).get_context_data()
        context['page_title'] = 'Главная | ELIS'
        return context


def assistance_homepage(request):
    return render(request, "index_assistance.html")
