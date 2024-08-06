from django.urls import include, path

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView,
                                            )

from .views import (CommentViewSet,
                    FollowViewSet,
                    GroupReadOnlyViewSet,
                    PostViewSet
                    )

router = SimpleRouter()
router.register('posts',
                PostViewSet,
                basename='post')
router.register('groups',
                GroupReadOnlyViewSet,
                basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comment')
router.register('follow',
                FollowViewSet,
                basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/jwt/create/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/jwt/verify/',
         TokenVerifyView.as_view(),
         name='token_verify'),
]
