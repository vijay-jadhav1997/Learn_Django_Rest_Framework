from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentRegister(admin.ModelAdmin):
  list_display = ('id', 'name', 'roll', 'city')