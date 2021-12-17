# Generated by Django 3.2.9 on 2021-12-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20211216_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_performer',
            field=models.CharField(choices=[('id=1', 'Messi'), ('id=2', 'Ronaldo'), ('id=3', 'Lewandowski'), ('id=4', 'Haaland'), ('id=5', 'Chiesa'), ('id=6', 'Benzema')], max_length=30, verbose_name='Task performers'),
        ),
    ]