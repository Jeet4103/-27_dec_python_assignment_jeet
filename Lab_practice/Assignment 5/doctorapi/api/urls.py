from django.contrib import admin
from django.urls import path, include
from .views import DoctorListCreateView, DoctorRetrieveUpdateDestroyView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),
]
