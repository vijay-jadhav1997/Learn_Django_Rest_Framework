from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import StudentModelViewSetAPI


#* Creating router object
router = DefaultRouter()

#* Register StudentViewSetAPI with Router
router.register('student2api', StudentModelViewSetAPI, basename='stud')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify_token'),
]
