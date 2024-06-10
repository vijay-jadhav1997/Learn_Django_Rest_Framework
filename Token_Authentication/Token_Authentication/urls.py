from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from api.views import StudentModelViewSetAPI


#* Creating router object
router = DefaultRouter()

#* Register StudentViewSetAPI with Router
router.register('student2api', StudentModelViewSetAPI, basename='stud')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gottoken/', obtain_auth_token),
]
