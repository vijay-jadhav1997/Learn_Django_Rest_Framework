from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def home(request):
  stud = Student.objects.get(id=1)
  print('\n\n 🌼', stud, stud.name)
  serializer = StudentSerializer(stud)
  print('\n\n ✨', serializer)
  print('\n\n 🙏🏻', serializer.data)
  json_data = JSONRenderer().render(serializer.data)
  print('\n\n 💯', json_data)

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
  