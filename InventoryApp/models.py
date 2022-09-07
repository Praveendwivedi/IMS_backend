from django.db import models

# Create your models here.
class Factories(models.Model):
    FactoryId   = models.AutoField(primary_key=True)
    FactoryName = models.CharField(max_length=50)
    Location    = models.CharField(max_length=50)

class Products(models.Model):
    Factory = models.ForeignKey(Factories,on_delete=models.CASCADE)
    ProductId = models.AutoField(primary_key=True)
    ProductName=models.CharField(max_length=50)
    Quantity = models.IntegerField() 
    Image = models.ImageField(upload_to="products",blank=True,null=True)
    Description=models.TextField(null=True,blank=True)
    
    # class Meta:
    #     abstract = True