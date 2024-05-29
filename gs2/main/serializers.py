from rest_framework import serializers

from main.models import Customer


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



