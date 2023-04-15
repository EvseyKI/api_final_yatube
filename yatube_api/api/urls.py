from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

Router_v1 = routers.DefaultRouter()
Router_v1.register('posts', PostViewSet, basename='posts')
Router_v1.register('groups', GroupViewSet, basename='groups')
Router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
Router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(Router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
