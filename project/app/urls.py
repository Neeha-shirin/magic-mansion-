from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.add_property, name='add_property'),
    path('properties/edit/<int:pk>/', views.edit_property, name='edit_property'),
    path('properties/delete/<int:pk>/', views.delete_property, name='delete_property'),
    path('properties/toggle-status/<int:pk>/', views.toggle_property_status, name='toggle_property_status'),
]
