from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.say_hello),
    path('index', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]