# Generated by Django 3.0.3 on 2020-03-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200311_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='one_task',
            name='time',
            field=models.DateField(),
        ),
    ]
