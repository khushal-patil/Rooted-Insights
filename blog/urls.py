from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
     path('create/', views.create_article, name='create_article'),
]
