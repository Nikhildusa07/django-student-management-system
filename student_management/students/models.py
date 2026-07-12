from django.db import models
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name