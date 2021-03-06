from django.urls import path
from . import views

urlpatterns = [

    path('posts/', views.home, name='home'),
    path('', views.main, name='main'),
    path('intro/popup/', views.popup, name='popup'),
    path('intro/', views.intro, name='intro'),
    path('create/', views.post_create, name='create'),
    path('<int:pk>/', views.post_detail, name='detail'),
    path('<int:pk>/update/', views.post_update, name='update'),
    path('<int:pk>/delete/', views.post_delete, name='delete'),
    path('<int:pk>/addcomment', views.comments, name='addcomment'),
]