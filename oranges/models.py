from django.db import models

# Create your models here.
class Orange(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'oranges'

