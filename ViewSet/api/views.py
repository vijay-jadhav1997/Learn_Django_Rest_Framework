from rest_framework.response import Response
from rest_framework import   viewsets, status

from .models import Student
from .serializers import StudentSerializer


#!ViewSet Class:
class StudentViewSetAPI(viewsets.ViewSet):
  def list(self, request):
    print("************** List *************")
    print("Basename:", self.basename)
    print("Action: ", self.action)
    print("Detail: ", self.detail)
    print("Suffix: ", self.suffix)
    print("Name: ", self.name)
    print("Description: ", self.description)
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk=None):
    print("************** Retrieve *************")
    print("Basename:", self.basename)
    print("Action: ", self.action)
    print("Detail: ", self.detail)
    print("Suffix: ", self.suffix)
    print("Name: ", self.name)
    print("Description: ", self.description)
    if pk is not None:
      student = Student.objects.get(pk=pk)
      serializer = StudentSerializer(student)
      return Response(serializer.data)

  def create(self, request):
    print("************** Create *************")
    print("Basename:", self.basename)
    print("Action: ", self.action)
    print("Detail: ", self.detail)
    print("Suffix: ", self.suffix)
    print("Name: ", self.name)
    print("Description: ", self.description)
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': "New student's admission is successful..!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def update(self, request, pk=None):
    print("************** Update *************")
    print("Basename:", self.basename)
    print("Action: ", self.action)
    print("Detail: ", self.detail)
    print("Suffix: ", self.suffix)
    print("Name: ", self.name)
    print("Description: ", self.description)
    if pk is not None:
      student = Student.objects.get(pk=pk)
      serializer = StudentSerializer(student, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response({'message':'Update Successful..!'}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def partial_update(self, request, pk=None):
    print("************** Partial_update *************")
    print("Basename:", self.basename)
    print("Action: ", self.action)
    print("Detail: ", self.detail)
    print("Suffix: ", self.suffix)
    print("Name: ", self.name)
    print("Description: ", self.description)
    if pk is not None:
      student = Student.objects.get(pk=pk)
      serializer = StudentSerializer(student, data=request.data, partial=True)
      if serializer.is_valid():
        serializer.save()
        return Response({'message':'Update Successful..!'}, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, pk=None):
    print("************** Destroy *************")
    print("Basename:", self.basename)
    print("Action: ", self.action)
    print("Detail: ", self.detail)
    print("Suffix: ", self.suffix)
    print("Name: ", self.name)
    print("Description: ", self.description)
    if pk is not None:
      student = Student.objects.get(pk=pk)
      student.delete()
      return Response({'message':'Deleted Successfully..!'}, status=status.HTTP_204_NO_CONTENT)




#! ModelViewSet Class:
class StudentModelViewSetAPI(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer


#! ReadOnlyModelViewSet Class:
class StudentReadOnlyModelViewSetAPI(viewsets.ReadOnlyModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

