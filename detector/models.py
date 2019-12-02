from django.db import models

# Create your models here.
class White(models.Model):
    url=models.CharField(max_length=500)
    