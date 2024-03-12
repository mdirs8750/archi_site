from django.contrib import admin
from .models import * #here we imposting only all table of models

#from .models import staffregistration # here we imposting only one table of model
# Register your models here.
admin.site.register(User_resgistration)
#admin.site.register(Staffregistration) # here we are creating registration of models we created (tables)
admin.site.register(Category)  # after registring go to views.py to work on the function in which you want to show or represent in html page
admin.site.register(Product)