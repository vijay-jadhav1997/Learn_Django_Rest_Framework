from rest_framework import serializers

from main.models import Customer


#* Validators :
def start_with_undercore(value):
  if value[0] == '_':
    raise serializers.ValidationError("Customer name can't start with '_'. It can only start with alphabet letters.")

class CustomerSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100, min_length=5)
  email = serializers.EmailField(max_length=50)
  password = serializers.CharField(min_length=8, max_length=20)


  def create(self, validated_data):
    return Customer.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    # print('\n\n 🎯 ', instance.name)
    # print(instance.email)
    # print(instance.password)

    instance.name = validated_data.get('name', instance.name)
    # print(instance.name)
    instance.email = validated_data.get('email', instance.email)
    # print(instance.email)
    instance.password = validated_data.get('password', instance.password)
    # print(instance.password)
    instance.save()
    return instance


  #* Field level validation
  def validate_name(self, value):
    if value.startswith('_'):
      raise serializers.ValidationError("Custome name can't start with '_' !")
    return value
  

  #* Object validator:
  def validate(self, data):
    # print(data)
    # print("Jay Hari ")
    if data.get('name')[0].lower() == 'a' and data.get('email')[-2 -1].lower() == 'in':
      raise serializers.ValidationError("Customer email can't ends with '.in' when the customer name satrt with letter 'a'.")
    return data




#* Model Serializer
class Customer2Serializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    # fields = ['name', 'email', 'password']
    fields = "__all__"
    # exclude = ['password']

    