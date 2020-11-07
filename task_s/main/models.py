from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Task(models.Model):
    title = models.CharField('Тема', max_length=50)
    task = models.TextField('Сообщение') #огромное множество текста

    # отправитель
    # сообщение, отправленное с аккаунта юзера, всегда будет направлено
    # админу
    sponsor = models.CharField('Отправитель', max_length=50, default='admin')
    #models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # получатель
    # админу необходимо указать кому отвечает или пишет сообщение
    recipient = models.CharField('Получатель', max_length=50, default='admin')
    #models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # if User =='admin':
        # sponsor = 'admin'
    #     recipient =  получаем из формы
    # elif User_аунтифирован:
    #     sponsor = 'user'
    #     recipient = 'admin'
    # else:
    #     'переправляем на логин'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        # verbose_plural = 'Задачи'
