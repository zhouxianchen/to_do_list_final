# Generated by Django 3.0.3 on 2020-03-14 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_auto_20200314_0455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
