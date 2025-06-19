from django.db import models

class Menu(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):   
    menu = models.ForeignKey(Menu,related_name='categories', on_delete=models.CASCADE,default=1)
    name= models.CharField(max_length=100)                                            
    def __str__(self):                                                              
        return f"{self.menu.name} -->{self.name}"

        

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product_images/',null=True,blank=True)
    specifications = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.category.name}" 
