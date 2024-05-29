from django.urls import path
from main import views


urlpatterns = [
  path('', views.home, name='home'),
  path('customer_create/', views.create_customer, name='customer_create'),
  path('customer_api/', views.customer_api, name='customer_api'),
  path('customer_class_api/', views.CustomerAPI.as_view(), name='customer_class_api'),
]