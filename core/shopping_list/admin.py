from django.contrib import admin

from .models import ShoppingItem

# Register your models here.
# @admin.register(ShoppingItem)
# class ShoppingItemAdmin(admin.ModelAdmin):
#   list_display = ['id', 'name', 'purchased']

admin.site.register(ShoppingItem)