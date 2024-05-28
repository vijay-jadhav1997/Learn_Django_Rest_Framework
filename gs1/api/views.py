from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import io

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

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
  if request.method == 'POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=python_data)

    if serializer.is_valid():
      serializer.save()
      response = {'message': 'Data Created'}
      json_response = JSONRenderer().render(response)
      return HttpResponse(json_response, content_type='application/json')
    
    json_response = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_response, content_type='application/json')
    