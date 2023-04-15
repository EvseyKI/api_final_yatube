from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы',
        help_text='Может состоять из символов и цифр',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор группы',
        help_text='Может состоять из кирилицы и цифр',
    )
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Краткое описание группы',
    )

    class Meta:
        verbose_name = 'Группа',
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title[:settings.LENGTH_TEXT]


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст поста',
        help_text='Пишите, что хотите в рамках приличия',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
        help_text='Это время создания даты, создается автоматически',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор текста',
        help_text='Пользователь, написавший текст',
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        verbose_name='Картинка',
        help_text='Расположена над текстом',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Название группы',
        help_text='Указывать необязательно',
    )

    class Meta:
        verbose_name = 'Запись',
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.text[:settings.LENGTH_TEXT]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Имя автора коментария',
        help_text='Это пользователь, написавший комментарий',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Название поста',
        help_text='Пост, к которому относится комментарий',
    )
    text = models.TextField(
        verbose_name='Пишем, что душе угодно',
        help_text='Пишем в рамках приличия',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата публикации комментария',
        help_text='Присваивается автоматически',
    )

    class Meta:
        verbose_name = 'Комментарий',
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:settings.LENGTH_TEXT]
