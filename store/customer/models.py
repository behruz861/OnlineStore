from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased = models.BooleanField(default=False)
    purchase_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name