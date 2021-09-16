from dashboard.blog.views import *
from dashboard.receipe.views import *
from dashboard.follower.views import *
from dashboard.author.views import *
from dashboard.views import *
from django.urls import path

urlpatterns = [
    path('', main_page, name='main_page'),

    path('blog/', blog_list, name='blog_list'),
    path('blog/<int:pk>/edit/>', blog_edit, name='blog_edit'),
    path('blog/create/', blog_create, name='blog_create'),
    path('blog/<int:pk>/delete/>', blog_delete, name='blog_delete'),

    path('recipe/', recipe_list, name='recipe_list'),
    path('recipe/create/', recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),

    path('follower/', followers_list, name='followers_list'),
    path('follower/create/', followers_create, name='followers_create'),
    path('follower/<int:pk>/edit/', followers_edit, name='followers_edit'),
    path('follower/<int:pk>/delete/', followers_delete, name='followers_delete'),

    path('author/', authors_list, name='authors_list'),
    path('author/create/', authors_create, name='authors_create'),
    path('author/<int:pk>/edit/', authors_edit, name='authors_edit'),
    path('author/<int:pk>/delete/', authors_delete, name='authors_delete'),
]