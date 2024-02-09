
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.main_page, name='main'),
    path('tech/', views.tech, name='tech'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('task/', views.task, name='task'),
    path('article/<slug:slug>/', views.article_page, name='article_page'),
    path('<str:group>/', views.group_page, name='group'),
]
