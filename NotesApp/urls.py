from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete)

]
