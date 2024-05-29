from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

from main.models import Customer
from main.serializers import CustomerSerializer


# Create your views here.
def home(request):
  users = Customer.objects.all()
  serializer = CustomerSerializer(users, many=True)
  json_data = JSONRenderer().render(serializer.data)
  return HttpResponse(json_data, content_type='application/json')


@csrf_exempt
def create_customer(request):
  if request.method == 'POST':
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = CustomerSerializer(data=python_data)
    if serializer.is_valid():
      serializer.save()
      res = {'msg': f'new customer ({python_data['name']}) is created'}
      json_res = JSONRenderer().render(res)
      return HttpResponse(json_res, content_type='json/application')

    json_res = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_res, content_type='json/application')



@csrf_exempt
def customer_api(request):
  if request.method == "GET":
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id', None)
    if id is not None:
      customer = Customer.objects.get(id=id)
      serializer = CustomerSerializer(customer)
    else:
      customer = Customer.objects.all()
      serializer = CustomerSerializer(customer, many=True)
    json_res = JSONRenderer().render(serializer.data)
    return HttpResponse(json_res, content_type='application/json')

  if request.method == "POST" :
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = CustomerSerializer(data=python_data)
    if serializer.is_valid():
      serializer.save()
      response = {'message': f'new Customer ({python_data['name']}) is created..! 🎯'}
    else:
      response = serializer.errors
    json_response = JSONRenderer().render(response)
    return HttpResponse(json_response, content_type='application/json')
      
  if request.method == 'PUT':
    data = request.body
    stream = io.BytesIO(data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    customer = Customer.objects.get(id=id)
    #* Complete Update - Required All Data from frontend/client.
    serializer = CustomerSerializer(customer, data=python_data)

    #* Partial Update - All Data is not required
    # serializer = CustomerSerializer(customer, data=python_data, partial=True)
    if serializer.is_valid():
      serializer.save()
      response = {'msg': f'the data of customer of id "{id}" is updated successfully...!! ✔👍🏻'}
      json_response = JSONRenderer().render(response)
    else:
      json_response = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_response, content_type='application/json')
      
  if request.method == 'DELETE':
    data = request.body
    stream = io.BytesIO(data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    customer = Customer.objects.get(id=id)
    customer.delete()
    response = {'message': f'The data of customer id "{id}" is deleted SUCCESSFULLY...!!'}
    # json_response = JSONRenderer().render(response)
    # return HttpResponse(json_response, content_type='application/json')
    return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='customer_class_api')
class CustomerAPI(View):
  def get(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id', None)
    if id is not None:
      customer = Customer.objects.get(id=id)
      serializer = CustomerSerializer(customer)
    else:
      customer = Customer.objects.all()
      serializer = CustomerSerializer(customer, many=True)
    json_res = JSONRenderer().render(serializer.data)
    return HttpResponse(json_res, content_type='application/json')

  def post(self, request, *args, **kwargs):
    json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    serializer = CustomerSerializer(data=python_data)
    if serializer.is_valid():
      serializer.save()
      response = {'message': f'new Customer ({python_data['name']}) is created..! 🎯'}
    else:
      response = serializer.errors
    json_response = JSONRenderer().render(response)
    return HttpResponse(json_response, content_type='application/json')
  
  def put(self, request, *args, **kwargs):
    data = request.body
    stream = io.BytesIO(data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    customer = Customer.objects.get(id=id)
    #* Complete Update - Required All Data from frontend/client.
    serializer = CustomerSerializer(customer, data=python_data)

    #* Partial Update - All Data is not required
    # serializer = CustomerSerializer(customer, data=python_data, partial=True)
    if serializer.is_valid():
      serializer.save()
      response = {'msg': f'the data of customer of id "{id}" is updated successfully...!! ✔👍🏻'}
      json_response = JSONRenderer().render(response)
    else:
      json_response = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_response, content_type='application/json')

  def delete(self, request, *args, **kwargs):
    data = request.body
    stream = io.BytesIO(data)
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    customer = Customer.objects.get(id=id)
    customer.delete()
    response = {'message': f'The data of customer id "{id}" is deleted SUCCESSFULLY...!!'}
    # json_response = JSONRenderer().render(response)
    # return HttpResponse(json_response, content_type='application/json')
    return JsonResponse(response, safe=False)
