from django.db import models


# Create your models here.
class Data(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Temperature in celcius')
    humidity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Humidity in percentage')
    gas = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Gas in pressure')

