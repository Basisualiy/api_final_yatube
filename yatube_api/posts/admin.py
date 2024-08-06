from django import forms
from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'image', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    search_fields = ('title', 'slug', 'description')
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'post', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ('user', 'following')

    def clean(self):
        cleaned_data = super().clean()
        if self.cleaned_data['user'] == self.cleaned_data['following']:
            raise forms.ValidationError('Нельзя подписываться на самого себя.')
        return cleaned_data


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    form = FollowForm
    list_display = ('pk', 'user', 'following')
    search_fields = ('user', 'following')
    empty_value_display = '-пусто-'
