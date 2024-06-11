from django.urls import path
from .views import *

urlpatterns = [
    path('', TodoHomepage.as_view(), name="todo_homepage"),
    path('add_space/', TodoAddSpace.as_view(), name="todo_add_space"),
    path('del_space/<int:space_id>', delete_space, name="todo_del_space"),
    path('add_table/<int:related_space_id>', TodoAddTable.as_view(), name="todo_add_table"),
    path('del_table/<int:pk>', delete_table, name="todo_del_table"),
    path('add_list/<int:pk>', TodoAddList.as_view(), name="todo_add_list"),
    # path('del_list/<int:pk>', del_list, name="todo_del_list"),
    path('add_task/<int:pk>', TodoAddTask.as_view(), name="todo_add_task"),
    # path('del_task/<int:pk>', del_task, name="todo_del_task"),
    path('table/<int:pk>', TodoTableDetail.as_view(), name="todo_table_info"),
]