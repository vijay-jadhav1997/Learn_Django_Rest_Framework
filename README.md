# ✨⚙🔄 Developing RESTful API with Django REST Framework 👩🏻‍💻💯🧗🏻‍♂️

## RESTful API :
- 


## Django REST Framework (DRF) :
- DRF is composed of the following components:

1. **Serializers :**
- In Django REST Framework, serializers are responsible for converting complex data such as Django QuerySets and model instances to native Python datatypes that can then be easily rendered into JSON, XML or other content types which is understandable by Front End.
> **Serialization :**  The process of converting complex data such as querysets & model instances to native Python datatypes are called **Serialization** in DRF.
> Django QuerySet ==> Python dictionaries ==> JSON

- Serializers are also responsible for deserialization which means it allows parsed data be converted back into complex types, after first validating the incoming data.
> **Deserialization :**  
> JSON ==> Python dictionaries ==> Django QuerySets

### DRF built-in serializer :
1. BaseSerializer
2. ModelSerializer
3. HyperlinkedModelSerializer
4. ListSerializer

- If our serializer maps closely to our model, it's best to use `ModelSerializer`.
2. **ModelSerializer :**
- The `ModelSerializer` class automatically created the serializer fields and validators from the corresponding model's fields (ex. User, Studentt, Task)
```py
# gs1/school/serializers.py
from rest_framework import serializers

from school.models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ["id", "name", "marks", "result"]
```


### Function Based api_view
### Class based APIView
### Generic APIView and Mixins
### Concrete View Class
| Single | Grouping Together|
|:----:|:------|
| ListAPIView | ListCreateAPIView |
| CreateAPIView | RetrieveUpdateAPIView|
| RetrieveAPIView | RetrieveDestroyAPIView|
| UpdateAPIView | RetrieveUpdateDestroyAPIView|
| DestroyAPIView | |

