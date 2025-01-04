from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='todo-detail'),
]