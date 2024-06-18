from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.renderers import JSONRenderer

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