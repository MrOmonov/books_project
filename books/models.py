from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=200)
    isbn = models.CharField(max_length=80)
    author = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.title