from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField('Задача', max_length=250)
    state = models.BooleanField('Статус выполнения', default=False)
    
    def __str__(self):
        return self.task
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'