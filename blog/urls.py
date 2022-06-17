from django.urls import path
from .views import LikeView,DisLikeView
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('dislike/<int:pk>', DisLikeView, name='dislike_post'),
    path('post/comment/<int:pk', views.post_comment, name='post_comment'),
    path('user',views.userpage, name='userpage')

]