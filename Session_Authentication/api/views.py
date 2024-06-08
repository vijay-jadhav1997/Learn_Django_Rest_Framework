from rest_framework.response import Response
from rest_framework import   viewsets, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from .models import Student
from .serializers import StudentSerializer
from .custom_permissions import MyPermission



#! ModelViewSet Class:
class StudentModelViewSetAPI(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [SessionAuthentication]
  # permission_classes = [IsAuthenticated]
  # permission_classes = [IsAuthenticatedOrReadOnly]
  # permission_classes = [DjangoModelPermissions]
  # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
  
  #! Custom permission class
  permission_classes = [MyPermission]


#! ReadOnlyModelViewSet Class:
class StudentReadOnlyModelViewSetAPI(viewsets.ReadOnlyModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes = [SessionAuthentication]
  permission_classes = [IsAdminUser]


#!ViewSet Class:
class StudentViewSetAPI(viewsets.ViewSet):

  def list(self, request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    if pk is not None:
      student = Student.objects.get(pk=pk)
      serializer = StudentSerializer(student)
      return Response(serializer.data)

  def create(self, request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': "New student's admission is successful..!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def update(self, request, pk=None):
    if pk is not None:
      student = Student.objects.get(pk=pk)
      serializer = StudentSerializer(student, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'message':'Update Successful..!'}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def partial_update(self, request, pk=None):
    if pk is not None:
      student = Student.objects.get(pk=pk)
      serializer = StudentSerializer(student, data=request.data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'message':'Update Successful..!'}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, pk=None):
    if pk is not None:
      student = Student.objects.get(pk=pk)
      student.delete()
      return Response({'message':'Deleted Successfully..!'}, status=status.HTTP_204_NO_CONTENT)

