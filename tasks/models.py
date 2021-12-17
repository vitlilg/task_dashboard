from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.


class UsersTasksModel(models.Model):
    users_performers = models.ManyToManyField(User,
                                              blank=True,
                                              help_text='Choice for task\'s performers',
                                              related_name="user_set",
                                              related_query_name="user")
    tasks_performers = models.ManyToManyField(Group,
                                              blank=True,
                                              related_name="group_set",
                                              related_query_name="group")

    class Meta:
        abstract = True

    def __str__(self):
        return self.users_performers


class TaskModel(UsersTasksModel):
    task_title = models.CharField(verbose_name='Task\'s title', max_length=64, null=True)
    task_text = models.TextField(verbose_name='Task\'s text', null=True)
    task_author = models.ForeignKey(User, verbose_name='Task\'s author', on_delete=models.CASCADE)
    task_create_date = models.DateTimeField(auto_now_add=True, null=True)
    task_update_date = models.DateTimeField(auto_now=True, null=True)
    task_image = models.ImageField(upload_to='tasks/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.task_title
