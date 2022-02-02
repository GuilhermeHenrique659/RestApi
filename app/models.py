from django.db import models

# Create your models here.

class Casa(models.Model):
    end=models.CharField(max_length=50,null=False)
    cidade=models.CharField(max_length=50, null=False)
    cep=models.CharField(max_length=10,null=False)
    preco=models.FloatField(null=False)

    def __str__(self):
        return self.preco