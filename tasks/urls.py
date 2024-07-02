from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('completion/<int:task_id>/', views.task_completion, name='task_completion'),
]
