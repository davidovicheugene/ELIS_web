from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoHomepage.as_view(), name="todo_homepage"),
    path('add_space/', TodoAddSpace.as_view(), name="todo_add_space"),
    path('del_space/<int:space_id>', delete_space, name="todo_del_space"),
    path('add_table/<int:related_space_id>', TodoAddTable.as_view(), name="todo_add_table"),
]