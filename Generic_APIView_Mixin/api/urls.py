from django.urls import path
from . import views


urlpatterns = [
  path('student_list/', views.StudentListAPI.as_view(), name='student_list'),
  path('student_create/', views.StudentCreateAPI.as_view(), name='student_create'),
  path('student_retrieve/<int:pk>/', views.StudentRetrieveAPI.as_view(), name='student_retrieve'),
  path('student_update/<int:pk>/', views.StudentUpdateAPI.as_view(), name='student_update'),
  path('student_destroy/<int:pk>/', views.StudentDestroyAPI.as_view(), name='student_destroy'),
  #? Group Views Urls =>
  path('student_list_create/', views.StudentListCreateAPI.as_view(), name='student_list_create'),
  path('student_actions/<int:pk>/', views.StudentUpdateRetrieveDestroyAPI.as_view(), name='student_destroy'),
]
