from django.db import models

# Create your models here.
class Client(models.Model):
    client_no = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100)
    owns_car = models.BooleanField()
    owns_realty = models.BooleanField()

    def __str__(self):
        return self.client_no