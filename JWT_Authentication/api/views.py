from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Student
from .serializers import StudentSerializer
from .custom_permissions import MyPermission



#! ModelViewSet Class:
class StudentModelViewSetAPI(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  # authentication_classes = [TokenAuthentication]
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  # permission_classes = [IsAuthenticatedOrReadOnly]
  
  #! Custom permission class
  # permission_classes = [MyPermission]

