from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('home/',home,name='home'),
    path('list/',tweet_list,name='tweet_list'),
    path('create/',create_tweet,name='tweet_create'),
    path('<int:tweet_id>/edit/',tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/',tweet_delete,name='tweet_delete')
]