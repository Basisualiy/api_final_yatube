from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

SIZE_OF_NAME = 25


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор поста')
    image = models.ImageField(
        upload_to='posts/', null=True, verbose_name='Изображение')
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL,
        verbose_name='Группа поста',
        related_name='posts', null=True
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:SIZE_OF_NAME]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Пост')
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers',
        verbose_name='Пользователь')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user',
        verbose_name='Подписчик')

    class Meta:
        unique_together = ('user', 'following')
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title[:SIZE_OF_NAME]
