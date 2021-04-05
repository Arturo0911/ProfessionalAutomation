from django.db import models


# Create your models here.

class Personal(models.Model):
    credentials = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    apartment = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    status = models.CharField(max_length=15)
    password = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'personal'
        verbose_name_plural = 'personal'

    def __str__(self):
        return self.name
