from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100, choices=[
        ('equipment', 'Equipment'),
        ('nutrition', 'Nutrition'),
        ('merchandise', 'Merchandise'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name