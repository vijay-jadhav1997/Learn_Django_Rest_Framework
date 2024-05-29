from django.contrib import admin
from main.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'password')

admin.site.register(Customer, CustomerAdmin)