from django.urls import path
from . import views 


urlpatterns = [
  (path('', views.home, name='home')),
  (path('students/', views.list_api, name='student_list')),
]
