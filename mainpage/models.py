from django.db import models

# Create your models here.

class Worker(models.Model):
    name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    salary = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name} {self.last_name}'

class PlantsModel(models.Model):
    plants_name = models.CharField(max_length=100, blank=False, default='Enter plant name')
    plants_amount = models.IntegerField(default=0)
    purchase_date = models.DateField()
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    def __str__(self):
        return f'{self.plants_name}'
