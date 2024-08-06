from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions, serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', 'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Follow
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        try:
            following = User.objects.get(
                username=self.initial_data['following']
            )
        except ObjectDoesNotExist:
            raise exceptions.ValidationError(
                f'Объект с username={self.initial_data["following"]}'
                ' не существует.', code=400
            )
        except KeyError:
            raise exceptions.ValidationError(
                {'following': ['Обязательное поле.']}, code=400
            )
        if user == following:
            raise exceptions.ValidationError(
                'Нельзя подписаться на самого себя!', code=400
            )
        if Follow.objects.filter(user=user, following=following).exists():
            raise exceptions.ValidationError(
                'У Вас уже есть родписка на '
                f'пользователя с username={following.username}', code=400
            )
        obj = Follow.objects.create(user=user, following=following)
        return obj
