from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_sticky_note, name='create_sticky_note'),
    path('read/<int:pk>/', views.read_sticky_note, name='read_sticky_note'),
    path('update/<int:pk>/', views.update_sticky_note, name='update_sticky_note'),
    path('delete/<int:pk>/', views.delete_sticky_note, name='delete_sticky_note'),
]
