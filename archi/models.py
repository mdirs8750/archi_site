from django.db import models



#{after cretaing MODEL[TABLE] register it to admin.py}


# Create your models here.
class User_resgistration(models.Model):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(default=0)
    contact_no=models.IntegerField(default=0)
    email=models.EmailField(max_length=100,null="True",blank="True")
    password=models.CharField(max_length=255,null="True",blank="True")

    def __str__(self):
        return self.first_name


# class Staffregistration(models.Model):
#     first_name=models.CharField(max_length=100,null=True,blank=True)
#     last_name=models.CharField(max_length=100,null=True,blank=True)
#     age=models.IntegerField(default=0)
#     contact_no=models.IntegerField(default=0)
#     email=models.EmailField(max_length=100,null="True",blank="True")
#     password=models.CharField(max_length=255,null="True",blank="True")


#     def __str__(self):
#         return self.first_name  #this is constuctor for showing entred data in admin page other wise it will show as (registration of object) user
    
class Category(models.Model):
    category_name=models.CharField(max_length=50,null="True",blank="True") #here we are creating the category names what types of product want to sell  & {after cretaing MODEL[TABLE] register it to admin.py}
    category_img=models.ImageField(upload_to="category/")   # in this field we are storing the image of category

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    prod_name=models.CharField(max_length=50,null="True",blank="True")
    prod_price=models.IntegerField(null="True")
    prod_image=models.ImageField(upload_to="product/")
    prod_discription=models.TextField(null="True")
    prod_category=models.ForeignKey(Category, on_delete=models.CASCADE) #this a foreign key because it showing a relationship between these two models, HERE USING CASCADE BECAUSE IT'S MEANS THAT 1 IF YOU DELETE A PRODUCT FROM A PRODUCT MODELS OR CATEGARY THEN THERE IS NO PROBLEM & IF YOU DELETE CATEGARY FROM PRODUCT MODELS THERE IS NO PRODUCT WILL BE LEFT ALL PRODUCT IS INSIDE THE CATEGARY. THIS JUST A SAFE CODE BLOCK FOR PRODUCT WHILE DELETEING PROFUCT { go to admin.py register your model}

    def __str__(name):
        return name.prod_name
    
