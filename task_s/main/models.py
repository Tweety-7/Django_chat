from django.db import models
from django.contrib.auth.models import User
from datetime import date

# class Sponsor(models.Model):
#     name = models.CharField('Отправитель', max_length=50, default='admin')
    # name = models.CharField('Отправитель')#,max_length=50, default='admin'

# class Recipient(models.Model):
#     name = models.CharField('Получатель', max_length=50, default='admin')

class Task(models.Model):
    title = models.CharField('Тема', max_length=50)
    task = models.TextField('Сообщение') #огромное множество текста

    #  у каждого сообщения есть только один отправитель и только один получатель
    # отправитель

    # сообщение, отправленное с аккаунта юзера, всегда будет направлено
    # админу
    sponsor = models.CharField('Отправитель', max_length=50, default='admin')
    #models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # sponsor = models.ManyToManyField(User)
    # получатель
    # админу необходимо указать кому отвечает или пишет сообщение
    # recipient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # recipient = models.CharField('Получатель', max_length=50, default='admin')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, default='admin', help_text='Получатель')
    # recipient = models.ManyToManyField(User)

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
