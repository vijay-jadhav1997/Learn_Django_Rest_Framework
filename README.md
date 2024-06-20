# ✨⚙🔄 Developing RESTful API with Django REST Framework 👩🏻‍💻💯🧗🏻‍♂️

## API (Application Programming Interface):
- An API is a set of rules and protocols for building and interacting with software applications.
- It allows different software systems to communicate with each other.

## REST (Representational State Transfer):
- REST is an architectural style for designing networked applications.
- It relies on a stateless, client-server communication protocol, typically HTTP.

### Key Principles of REST:

1. Stateless: Each request from a client to server must contain all the information needed to understand and process the request. The server does not store any state about the client session.
2. Client-Server: The client and server are separate entities, each responsible for different tasks. The client handles the user interface and user experience, while the server handles data storage and business logic.
3. Cacheable: Responses from the server can be cached by clients to improve performance.
4. Uniform Interface: RESTful APIs have a consistent way of communicating, often using HTTP methods like GET, POST, PUT, and DELETE.
5. Layered System: A client cannot ordinarily tell whether it is connected directly to the end server or to an intermediary along the way.

#### RESTful API :
- A RESTful API is an API that adheres to the principles of REST.
- It uses HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources.

#### HTTP Methods:
1) GET: Retrieve data from the server (e.g., get a list of users).
2) POST: Send data to the server to create a new resource (e.g., create a new user).
3) PUT: Update an existing resource on the server (e.g., update user details).
4) DELETE: Remove a resource from the server (e.g., delete a user).


### Following are the steps to create a simple RESTful API using Django REST Framework:
1. Setting up the Django project and app.
2. Creating a model for the data.
3. Creating serializers to convert model instances to JSON.
4. Creating views to handle API requests.
5. Setting up URL routing to access the API.



## Django REST Framework (DRF) :
- DRF is composed of the following components:

1. **Serializers :**
- In Django REST Framework, serializers are responsible for converting complex data such as Django QuerySets and model instances to native Python datatypes that can then be easily rendered into JSON, XML or other content types which is understandable by Front End.
> **Serialization :**  The process of converting complex data such as querysets & model instances to native Python datatypes are called **Serialization** in DRF.
> Django QuerySet/Model Instance ==> Python dictionaries ==> JSON

```py
  def student_list_api(request):
    """
    List all the students, or create a new instance of Student model.
    """
    if request.method == "GET":
      students = Student.objects.all()
      py_data = StudentSerializer(students, many=True) # serialization
      return JsonResponse(py_data, safe=False) # safe=False allows non-dictionary object.
    
    elif request.method == "POST":
      stream = io.BytesIO(request.body)
      py_data = JSONParser().parse(py_data)
      serializer = StudentSerializer(data=py_data) # de-serialization
      if serializer.is_valid():
        serializer.save()
        message_response = {'messagge':'New student is added successfully'}
        return JsonResponse(message_response)
```

- Serializers are also responsible for deserialization which means it allows parsed data be converted back into complex types, after first validating the incoming data.
> **Deserialization :**  
> JSON ==> Python dictionaries ==> Django QuerySets/Model Instance

### DRF built-in serializer :
1. BaseSerializer
2. ModelSerializer
3. HyperlinkedModelSerializer
4. ListSerializer

1. **Serializer :**
- Serializers provide complete control over how we define and handle the conversion between complex types and JSON. They are highly customizable and do not assume the existence of a Django model.

```py
class StudentSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  name = serializers.CharField(max_length=100)
  roll = serializers.IntegerField()
  city = serializers.CharField(max_length=100)

  def create(self, validated_data):
    # Create and return a new `Student` instance.
    return Student.objects.create(**validated_data)


  def update(self, instance, validated_data):
    # Update and return an existing `Student` instance.
    instance.name = validated_data.get('name', instance.name)
    instance.roll = validated_data.get('roll', instance.roll)
    instance.city = validated_data.get('city', instance.city)
    instance.save()
    return instance
```
**Use cases of Serializers:**
- When we need full control over the serialization/deserialization process.
- When dealing with non-model data or complex data structures.
- When we need to implement custom validation or field-level operations.


- If our serializer maps closely to our model, it's best to use `ModelSerializer`.
2. **ModelSerializer :**
- `ModelSerializers` are a subclass of serializers that provide a shortcut for creating serializers that deal with Django models. 
- Automatic Fields: Fields are generated based on the model's fields, reducing manual configuration.
- Built-in Validations: Utilizes model field validations automatically.
- Default CRUD Methods: Provides default create and update methods based on the model.

```py
# gs1/school/serializers.py
from rest_framework import serializers

from school.models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ["id", "name", "marks", "result"]
    # fields = "__all__"
```

**Use cases of Serializers:**
- When we want to quickly create serializers for our Django models with minimal configuration.
- When we are working directly with Django models and need to serialize/deserialize model instances.
- When we want to leverage DRF's built-in validation based on model fields.


### Best Practices in DRF:
1. Use @api_view for simple function-based views.
2. Use APIView for more complex views with better structure.
3. Use ViewSet and Router for large applications with standard CRUD operations.

### Function Based api_view
### Class based APIView
 - DRF’s class-based views provide more structure and are better for more complex APIs.

 ```py
 from rest_framework.views import APIView
  from rest_framework.response import Response
  from rest_framework import status
  from .models import Student
  from .serializers import StudentSerializer

  class StudentListView(APIView):
    def get(self, request):
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)
      return Response(serializer.data)

```

### Generic APIView and Mixins
### Concrete View Class
| Single | Grouping Together|
|:----:|:------|
| ListAPIView | ListCreateAPIView |
| CreateAPIView | RetrieveUpdateAPIView|
| RetrieveAPIView | RetrieveDestroyAPIView|
| UpdateAPIView | RetrieveUpdateDestroyAPIView|
| DestroyAPIView | |

