from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('profile/edit/',
         views.ProfileEditView.as_view(), name='edit_profile'),
    path('profile/<slug:username>/',
         views.ProfileView.as_view(), name='profile'),
    path('posts/create/',
         views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/',
         views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/',
         views.PostEditView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete/',
         views.PostDeleteView.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/',
         views.CommentCreateView.as_view(), name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:pk>/',
         views.CommentEditView.as_view(), name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:pk>/',
         views.CommentDeleteView.as_view(), name='delete_comment'),
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),
]
