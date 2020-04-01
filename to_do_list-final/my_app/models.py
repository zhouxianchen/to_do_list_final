from django.db import models


class Big_subject(models.Model):
    # choices = ((1, '管理工作'), (2, '后装工作'), (3, '政治工作'))

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, )
    big_subject = models.ForeignKey(to='Big_subject', on_delete=models.CASCADE, blank=True, related_name='tasks')

    class Meta:
        unique_together = ('name', 'big_subject')

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    task = models.ForeignKey(to='Task', on_delete=models.CASCADE, related_name='activities')
    progress = models.CharField(max_length=50)
    start_time = models.DateField(max_length=50, blank=True)
    end_time = models.DateField(max_length=50, blank=True)

    def __str__(self):
        return self.name

