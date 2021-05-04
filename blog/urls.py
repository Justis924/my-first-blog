from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('conv/', views.conv, name='conv'),
  path('info/', views.info, name='info'),
  path('news/', views.news, name='news'),
  path('topic/', views.topic, name='topic'),

]
