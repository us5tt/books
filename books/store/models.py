from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    autor_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}: {self.price}: {self.autor_name}'

