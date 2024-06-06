from django.urls import path
from .views import *

urlpatterns = [
    path('', AssistanceHomepage.as_view(), name="assistance_homepage"),

]