from django.urls import path
from .views import *

urlpatterns = [
    path('', assistance_homepage, name="assistance_homepage"),

]