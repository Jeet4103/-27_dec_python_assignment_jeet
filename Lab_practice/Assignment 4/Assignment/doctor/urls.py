from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('about/', views.about, name='about'), 
    path('category/<str:category_name>/', views.category_view, name='category'),
    path('doctors_admin/', views.doctors_admin, name='doctors_admin'),
    path('doctor/<int:doctor_id>/edit/', views.edit_doctor, name='edit_doctor'),
    path('doctor/<int:doctor_id>/delete/', views.delete_doctor, name='delete_doctor'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),

      # Adjust according to your views
]
