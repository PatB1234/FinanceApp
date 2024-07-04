from django.db import models

# Create your models here.


class User(models.Model):

    name = models.TextField()
    email = models.TextField()
    password = models.TextField()

    def __str__(self):

        return str(self.id)
