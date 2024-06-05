from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from api.views import StudentViewSetAPI, StudentModelViewSetAPI, StudentReadOnlyModelViewSetAPI


#* Creating router object
router1 = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()

#* Register StudentViewSetAPI with Router
router1.register('student1api', StudentViewSetAPI, basename='student')
router2.register('student2api', StudentModelViewSetAPI, basename='stud')
router3.register('student3api', StudentReadOnlyModelViewSetAPI, basename='read_only-student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router1.urls)),
    path('stu/', include(router2.urls)),
    path('stu-read-only/', include(router3.urls)),
]
