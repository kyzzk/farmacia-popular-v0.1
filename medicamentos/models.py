from django.db import models

class Medicamento(models.Model):
    name = models.CharField(max_length=100)
    mg = models.IntegerField()
    indication = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

