from django.db import models
from django.contrib.auth import get_user_model
from hw01.settings import GROUPS


User = get_user_model()


class Contact(models.Model):
    name = models.CharField(
        'Имя',
        max_length=100
    )
    title = models.CharField(
        'Заголовок',
        max_length=250
    )
    text = models.TextField(
        'Текст'
    )
    email = models.EmailField(
        'Почта'
    )
    date = models.DateTimeField(
        'Время отправки',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return self.title[:50]

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Письмо от пользователя'
        verbose_name_plural = 'Письма от пользователей'

class Article(models.Model):
    title = models.TextField(
        'Заголовок'
    )
    text = models.TextField(
        'Текст'
    )
    slug = models.SlugField(
        'Слаг',
        unique=True
    )
    pub_date = models.DateTimeField(
        'Время публикации',
        auto_now_add=True,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.CharField(
        choices=GROUPS,
        max_length=150,
        verbose_name='Раздел'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='images/',
        blank=True
    )

    def __str__(self):
        return self.title[:50]

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
