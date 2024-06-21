import io

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer

# Create your views here.
def home(request):
  if request.method == 'GET':
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data, serializer.data, serializer, sep="\n")
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data, safe=False)
  # return HttpResponse("<h1>Jay Shree Ram</h1>")
  return HttpResponse("Shree Vitthal Rakhumai")



@csrf_exempt
def list_api(request):
  """
    List all students, or create a new student.
  """
  if request.method == "GET":
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == "POST":
    stream = io.BytesIO(request.body)
    py_data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=py_data)
    if serializer.is_valid():
      serializer.save()
      # json_response = JSONRenderer().render({'message': 'New instance is created successfully.'})
      return JsonResponse({'message': 'New instance is created successfully.'})



@api_view(['GET', 'POST'])
def student_list_api(request):
  pass