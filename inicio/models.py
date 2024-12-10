from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    
    def __str__(self):
        return f'Auto({self.id}): {self.marca} {self.modelo} {self.anio}'