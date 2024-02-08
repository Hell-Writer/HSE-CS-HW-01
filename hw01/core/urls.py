
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.main_page, name='main'),
    path('tech/', views.tech, name='tech'),
    path('contact/', views.contact, name='contact'),
    path('author/', views.author, name='author'),
    path('task/', views.task, name='task'),
    path('<str:group>/', views.group_page, name='group'),
]
