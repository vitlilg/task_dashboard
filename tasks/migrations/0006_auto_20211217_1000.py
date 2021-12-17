# Generated by Django 3.2.9 on 2021-12-17 08:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_auto_20211217_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='task_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.usertaskmodel', verbose_name="Task's author"),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='task_performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]