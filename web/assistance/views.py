from django.shortcuts import render


def assistance_homepage(request):
    return render(request, "index_assistance.html")
