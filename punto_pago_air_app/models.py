from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=125)

    def __str__(self):
        return f"{self.code}  - {self.name}"