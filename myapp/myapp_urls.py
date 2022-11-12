from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add_post/',views.add_article,name="add_article"),

    path('dashboard/',views.dashboard,name="dashboard"),
    
    path('edit_article/<int:id>',views.edit_article,name="edit_article"),
    path('confirm_delete/<int:id>',views.delete_confirm,name="delete_confirm"),
    path('article_detail/<int:id>',views.article_detail,name="article_detail"),

    path('delete_article/<int:id>',views.delete_article,name="delete_article"),
    path('home/',views.home,name="home"),
    path('author_list/',views.author_list,name="author_list"),
    path('title_list/',views.title_list,name="title_list"),
    path('author_article/<int:id>',views.author_article,name="author_article"),
    path('article_on_topic/<topic>',views.article_on_topics,name="article_on_topic"),
]