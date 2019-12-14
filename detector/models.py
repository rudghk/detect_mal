from django.db import models

# Create your models here.
<<<<<<< HEAD
class Black(models.Model):
    black_id = models.CharField(max_length = 100)
    url = models.CharField(max_length = 500)

    def __str__ (self):
        self.black_id


class White(models.Model):
    url = models.CharField(max_length=500)
=======
class White(models.Model):
    url=models.CharField(max_length=500)
>>>>>>> ec526d6fa3b2119d5451389f0654577e7a6ead34
    