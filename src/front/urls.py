from django.urls import path
from front.views.blogpost_views import blog_post
from front.views.receipes import recipes
from front.views.receipe_post import recipes_post
from front.views.contacts import contact
from front.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("blog_post/", blog_post, name="blog_post"),
    path("recipes/", recipes, name="recipes"),
    path("recipes_post/", recipes_post, name="recipes_post"),
    path("contact/", contact, name="contact")
]
