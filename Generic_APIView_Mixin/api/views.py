from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, RetrieveModelMixin


from api.models import Student
from api.serializers import StudentSerializer


#* GenericAPIView and Model Mixins

class StudentListAPI(ListModelMixin, GenericAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)
  

class StudentCreateAPI(CreateModelMixin, GenericAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
  

class StudentRetrieveAPI(RetrieveModelMixin, GenericAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)
  
  
class StudentUpdateAPI(UpdateModelMixin, GenericAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)
  

class StudentDestroyAPI(DestroyModelMixin, GenericAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)



#? Grouping List and Create class together - Which don't need PK
class StudentListCreateAPI(GenericAPIView, CreateModelMixin, ListModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


#? Grouping Update, Retrieve and Destroy class together - They all need pk
class StudentUpdateRetrieveDestroyAPI(GenericAPIView, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)