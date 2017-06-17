from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=80, unique=True)
    f_color = models.CharField(max_length=7)
    f_animal = models.CharField(max_length=3)

    def __str__(self):
        return self.name
