from django.db import models
from django.contrib.auth import get_user_model
from hw01.settings import GROUPS


User = get_user_model()


class Article(models.Model):
    title = models.TextField(
        'Заголовок',
        help_text='Введите заголовок'
    )
    text = models.TextField(
        'Текст',
        help_text='Введите текст'
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
        verbose_name='Раздел',
        help_text='Выберите раздел'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='images/',
        blank=True,
        help_text='Прикрепите картинку'
    )

    def __str__(self):
        return self.title[:50]

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
