from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

SIZE_OF_NAME = 25


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL,
        verbose_name='Группа поста',
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return self.text[:SIZE_OF_NAME]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')


class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField('Слаг', unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title[:SIZE_OF_NAME]
