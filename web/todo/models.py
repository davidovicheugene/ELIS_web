from django.db import models


class TodoSpace(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=512, blank=True, verbose_name="Описание")
    logo = models.ImageField(upload_to="media/uploads/todo/space_avatars/", blank=True, verbose_name="Логотип")
    user = models.ForeignKey('users.ImpUser', on_delete=models.CASCADE, verbose_name="Создатель")
    tables_count = models.IntegerField(default=0, verbose_name="Кол-во досок")
#     TODO:members(many to many or one to many)

    def __str__(self):
        return f"{self.user.username}: {self.title}"


class TodoTable(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=512, blank=True, verbose_name="Описание")
    related_space = models.ForeignKey(TodoSpace, on_delete=models.CASCADE, verbose_name="Пространство")
    user = models.ForeignKey('users.ImpUser', on_delete=models.CASCADE, verbose_name="Создатель")
    lists_count = models.IntegerField(default=0, verbose_name="Кол-во списков")
#     TODO:background
#     TODO:admin

    def __str__(self):
        return f"{self.title}"


class TodoList(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    related_table = models.ForeignKey(TodoTable, on_delete=models.CASCADE, verbose_name="Доска")
    user = models.ForeignKey('users.ImpUser', on_delete=models.CASCADE, verbose_name="Создатель")
    tasks_count = models.IntegerField(default=0, verbose_name="Кол-во задач")

    def __str__(self):
        return f"{self.title} | {self.user.username}"


class TodoTask(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=10000, blank=True, verbose_name="Описание")
    label = models.CharField(max_length=20, blank=True, verbose_name="Метка")
    related_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, verbose_name="Список")
    related_table = models.ForeignKey(TodoTable, on_delete=models.CASCADE, verbose_name="Доска")
    user = models.ForeignKey('users.ImpUser', on_delete=models.CASCADE, verbose_name="Создатель")


class TodoAttachment(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    file = models.FileField(upload_to="media/uploads/todo/attachments/", verbose_name="Файл")
    related_task = models.ForeignKey(TodoTask, on_delete=models.CASCADE, verbose_name="Задача")
    user = models.ForeignKey('users.ImpUser', on_delete=models.CASCADE, verbose_name="Создатель")

