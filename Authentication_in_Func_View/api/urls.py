from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('<int:stud_id>', views.home, name='home'),
  path('students/', views.students_info, name='students'),
  path('student_create/', views.student_create, name='stdent_create'),
  # path('students/<int: stud_id>', views.students_info, name='students'),
  path('jay_hari/', views.jay_hari, name='jay_hari'),
  path('om_shree/', views.om_shree, name='om_shree'),
  path('namo_narayan/', views.namo_narayan, name='namo_narayan'),
  path('namo_narayan/<int:stud_id>/', views.namo_narayan, name='namo_narayan'),
  path('har_har/', views.StudentAPI.as_view(), name='har_har'),
  path('har_har/<int:stud_id>/', views.StudentAPI.as_view(), name='har_har'),
]
