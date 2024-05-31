from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import io

from .models import Student
from .serializers import StudentSerializer

# Create your views here.
def home(request):
  stud = Student.objects.get(id=1)
  # print('\n\n 🌼', stud, stud.name)
  serializer = StudentSerializer(stud)
  # print('\n\n ✨', serializer)
  # print('\n\n 🙏🏻', serializer.data)
  json_data = JSONRenderer().render(serializer.data)
  # print('\n\n 💯', json_data)

  return HttpResponse(
    json_data, content_type='application/json'
  )

def students_info(request):
  students = Student.objects.all()
  serializer = StudentSerializer(students, many=True)

  # data_ = JSONRenderer().render(serializer.data)
  # return HttpResponse(data_)

  return JsonResponse(serializer.data, safe=False)
  

def student_data(request, stud_id):
  students = Student.objects.all()
  serializer = StudentSerializer(students, many=True)

  data_ = JSONRenderer().render(serializer.data)
  # return HttpResponse(data_)

  return JsonResponse(serializer.data)
  
@csrf_exempt
def student_create(request):
  if request.method == 'GET':
    data = request.body
    stream = io.BytesIO(data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id', None)
    if id is not None:
      students = Student.objects.get(id=id)
      serializer = StudentSerializer(students)
    else:  
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

  
  if request.method == 'POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=python_data)

    if serializer.is_valid():
      serializer.save()
      response = {'message': f'New student name {python_data.get('name')}, admission successfully completed!🎉✨'}
      json_response = JSONRenderer().render(response)
      return HttpResponse(json_response, content_type='application/json')
    
    json_response = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_response, content_type='application/json')
    


@api_view(['GET', 'POST'])
def jay_hari(request):
  if request.method == 'GET':
    return Response({'message': '!! ...Jay Jay Ram krushna Hari... !!'})

  if request.method == 'POST':
    # stream = io.BytesIO(request.body)
    # data = JSONParser().parse(stream)
    print('\n\n 💥🌼 ', request.headers, "\n\n 💯 ", request.body)
    return Response({**request.data})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def om_shree(request):
  if request.method == 'GET':
    id = request.data.get('id')
    if id is not None:
      student = Student.objects.get(id=id)
      serializer = StudentSerializer(student)
    else:
      student = Student.objects.all()
      serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)
      # return Response({'message': '!! ...Jay Jay Ram krushna Hari... !!'})

  if request.method == 'POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message':'Admission of the new student is successful.. 🌼🎉'})
    return Response(serializer.errors)
  

  if request.method == "PUT":
    id = request.data.get('id')
    student = Student.objects.get(id=id)
    serializer = StudentSerializer(student, data=request.data)
    # serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': f"The data of student id '{id}' is updated successfully...🎉💯"})
    return Response(serializer.errors)


  if request.method == "DELETE":
    id = request.data.get('id')
    student = Student.objects.get(id=id)
    student.delete()
    return Response({'message': f"The student id '{id}' is deleted successfully... ❌💯"})



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def namo_narayan(request, stud_id=None):
  if request.method == 'GET':
    if stud_id is not None:
      student = Student.objects.get(pk=stud_id)
      serializer = StudentSerializer(student)
    else:
      student = Student.objects.all()
      serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)
      # return Response({'message': '!! ...Jay Jay Ram krushna Hari... !!'})

  if request.method == 'POST':
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message':'Admission of the new student is successful.. 🌼🎉'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  if request.method == "PUT":
    student = Student.objects.get(pk=stud_id)
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': f"The data of student id '{stud_id}' is updated successfully...🎉💯"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  if request.method == "PATCH":
    student = Student.objects.get(pk=stud_id)
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response({'message': f"The data of student id '{stud_id}' is updated successfully...🎉💯"}, status=status.HTTP_206_PARTIAL_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



  if request.method == "DELETE":
    student = Student.objects.get(pk=stud_id)
    student.delete()
    return Response({'message': f"The student id '{stud_id}' is deleted successfully... ❌💯"})

