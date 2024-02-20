from django.urls import path
from . import views

urlpatterns = [
    path('todoApp/', views.todoApp, name='todoApp'),
]
