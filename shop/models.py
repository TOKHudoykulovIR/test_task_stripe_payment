from django.db import models
from django.urls import reverse

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('api:item-detail', args=[str(self.id)])
