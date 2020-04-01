# Generated by Django 3.0.3 on 2020-03-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_auto_20200314_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='task',
            unique_together={('name', 'big_subject')},
        ),
    ]
