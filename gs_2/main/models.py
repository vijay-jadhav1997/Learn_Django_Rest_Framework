from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=100, unique=True)
  email = models.EmailField(max_length=50)
  password = models.CharField(max_length=20)

  def __str__(self):
    return self.name
