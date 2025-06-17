from django.db import models

class Menu(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):   # Jab hum parent model se child model ke records ko access karte hain, using the related_name.
    menu = models.ForeignKey(Menu,related_name='categories', on_delete=models.CASCADE,default=1)#ye bata raha hai ki category kis Menu(parent class ki child class hai)
    name= models.CharField(max_length=100)                                            #related_name inbuilt keyword hai jo ki model se sari category lane ka kam 
    def __str__(self):                                                              #iska use serializers me hota hai 
        return f"{self.menu.name} -->{self.name}"

        # Haan, related_name Django ka inbuilt keyword hai jo ForeignKey me use hota hai.
#Ye batata hai ki reverse relation ka naam kya hoga — yani agar aap Menu object se uski categories access karna chahein to kis naam se karein.

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product_images/',null=True,blank=True)
    specifications = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.category.name}" 