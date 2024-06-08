from django.db import models


class TodoSpace(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=512, blank=True, verbose_name="Описание")
    logo = models.ImageField(upload_to="media/uploads/todo/space_avatars/", default="static/img/icons/base/no-image.png"
                             , verbose_name="Логотип")
#     TODO:members(many to many or one to many)


class TodoTable(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=512, blank=True, verbose_name="Описание")
    related_space = models.ForeignKey(TodoSpace, on_delete=models.CASCADE, verbose_name="Пространство")
#     TODO:background
#     TODO:admin


class TodoList(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    related_table = models.ForeignKey(TodoTable, on_delete=models.CASCADE, verbose_name="Доска")


class TodoTask(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=10000, blank=True, verbose_name="Описание")
    label = models.CharField(max_length=20, blank=True, verbose_name="Метка")
    related_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, verbose_name="Список")


class TodoAttachment(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    file = models.FileField(upload_to="media/uploads/todo/attachments/", verbose_name="Файл")
    related_task = models.ForeignKey(TodoTask, on_delete=models.CASCADE, verbose_name="Задача")

