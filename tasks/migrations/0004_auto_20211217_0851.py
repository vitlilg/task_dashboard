# Generated by Django 3.2.9 on 2021-12-17 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0003_alter_task_task_performer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=64, null=True, verbose_name="Task's title")),
                ('task_text', models.TextField(null=True, verbose_name="Task's text")),
                ('task_limit_days', models.DurationField(blank=True, help_text='Max duration of days for this task', null=True)),
                ('task_create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('task_update_date', models.DateTimeField(auto_now=True, null=True)),
                ('task_image', models.ImageField(null=True, upload_to='tasks/%Y/%m/%d/')),
                ('task_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Task's author")),
            ],
        ),
        migrations.CreateModel(
            name='UsersTaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.group')),
                ('task', models.ManyToManyField(to='tasks.TaskModel')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='task_performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.userstaskmodel'),
        ),
    ]
