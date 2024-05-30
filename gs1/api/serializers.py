from rest_framework import serializers

from .models import Student

#* Validators
def start_with_r(value):
  if value[0].lower() != 'r':
    raise serializers.ValidationError("Name should start with R.")

class StudentSerializer(serializers.Serializer):
  name = serializers.CharField( max_length=70, validators=[start_with_r])
  roll = serializers.IntegerField( )
  city = serializers.CharField( max_length=70)

  def create(self, validate_data):
    return Student.objects.create(**validate_data)
  
  def validate_roll(self, value):
    # print(value)
    if value >= 200:
      raise serializers.ValidationError("Admission has been closed !")
    return value

  def validate(self, data):
    # print(data)
    if data.get('name').lower().startswith('p') and data.get('roll') > 50:
      raise serializers.ValidationError(f"When Student name start with 'p', the roll number must be less than 50 💯")
    return data