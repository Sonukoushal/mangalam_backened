from django.db import models
from django.conf import settings
from products.models import Product

class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user','product']

    def __str__(self):
        return f"{self.user.username} favourited {self.product.name}"