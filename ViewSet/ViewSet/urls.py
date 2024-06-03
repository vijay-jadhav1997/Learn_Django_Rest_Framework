from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.views import StudentViewSetAPI


#* Creating router object
router = DefaultRouter()

#* Register StudentViewSetAPI with Router
router.register('studentapi', StudentViewSetAPI, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
