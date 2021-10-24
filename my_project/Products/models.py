from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.IntegerField()
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    update_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name