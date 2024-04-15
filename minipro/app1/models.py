from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Category(models.Model):
     name=models.CharField(max_length=100,primary_key=True)
     img=models.ImageField(null=True,unique=True)
     
     
     def __str__(self):
          return self.name
     
class Brand(models.Model):
     cat=models.ForeignKey(Category,on_delete=models.CASCADE)
     bname=models.ForeignKey(max_length=100,primary_key=True)  
     


class Item(models.Model):
     cat=models.ForeignKey(Category,on_delete=models.CASCADE)
     brname=models.ForeignKey(Brand,on_delete=models.CASCADE)
     iname=models.CharField(max_length=100,primary_key=True)  
     des=models.TextField(null=True)
     avaibality=models.CharField(max_length=50)
     price=models.IntegerField()
     type=models.TextField(null=True)
     imgage=models.ImageField(null=True,unique=True)
     

     def __str__(self):
          return self.iname

