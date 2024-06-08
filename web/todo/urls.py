from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoHomepage.as_view(), name="todo_homepage"),

]