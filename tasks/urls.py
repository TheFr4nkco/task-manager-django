from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('create/', views.task_create_view, name='task_create'),
    path('update/<int:pk>/', views.task_update_view, name='task_update'),
    path('delete/<int:pk>/', views.task_delete_view, name='task_delete'),
    path('toggle/<int:pk>/', views.task_toggle_view, name='task_toggle'),
]
