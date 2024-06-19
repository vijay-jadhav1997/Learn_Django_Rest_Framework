from rest_framework import serializers

# from .serializers import Student



# 
class StudentSerializer(serializers.Serializer):
  name = serializers.CharField(max_length=100)
  roll = serializers.IntegerField()
  city = serializers.CharField(max_length=100)

  pass




# class StudentSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Student
#     fields = "__all__"