from django.db import models

# Create your models here.
class Product(models.Model):
    name: str = models.TextField()
    price: float = models.FloatField(default=0.0)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Product: {self.name}"
    
