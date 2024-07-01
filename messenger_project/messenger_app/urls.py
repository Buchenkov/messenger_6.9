from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .views import register, PostListView, ProfileViewSet, UserCreateView, UserDetailView, \
    PostListCreateView, CommentCreateView, post_detail  # ChatViewSet, MessageViewSet,

router = DefaultRouter()
# router.register(r'chats', ChatViewSet)
# router.register(r'messages', MessageViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    path('register/', register, name='register'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('', PostListView.as_view(), name='post_list'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('post/create/', views.post_create, name='post_create'),
]

