from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('students/', views.students_info, name='students'),
  # path('students/<int: stud_id>', views.students_info, name='students'),
]
