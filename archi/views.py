from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
#for password makinf and checkingf
from django.contrib.auth.hashers import check_password, make_password

from .models import * # here import all tables created in models to save user data 
# Create your views here.
#function for calling your first webpage
"""def base(request):
    return render(request,'base.html')"""

#this function for home, Category, Product full functioning
def home(request):
    # now we are going to fetch catogary details
    fetch_category=Category.objects.all() 

    cate_id=request.GET.get("category_id")
    if cate_id:
        fetch_product=Product.objects.filter(prod_category=cate_id)
    else:
        fetch_product=Product.objects.all()
    
    #fetch_product=Product.objects.all()
    
    context={
        'category':fetch_category,
        'feproduct':fetch_product
    }
    return render(request, 'home.html',context=context)

#this for home render or for showing the catogary you want show incomplete for product but working
# def home(request):
#     # now we are going to fetch catogary details
#     fetch_category=category.objects.all() #we are cretaong object for fetching the models details after this go to [setting.py] to add images visible to site
#     context={
#         "category":fetch_category  # THIS WILBE USABLE FOR FOR LOOP TO FFETCH DETAIL FOR WEB PAGE
#     }
#     return render(request,'home.html', context=context)


# function for home page this for first time just to configure working or not how its's
def testinghtml(request):
    if request.method=='POST':
        first_nam=request.POST.get("fname")# here fname is input's name attribute value
        last_nam=request.POST.get("lname")
    
        print(first_nam,"   ",last_nam)# for dbubg that input value is coming here or
    return render(request,  'testinghtml.html')
#         cl_obj=staffregistration(   #code for saveing data 
#             first_name=first_nam,
#             last_name=last_nam,
#         )
#         cl_obj.save() #here your data is saving in your database

        # return render(request,"home.html",{'key':fetch_data})
    # this fetch all data of your tables but ina quesry set <QuerySet [<staffregistration: asd>, <staffregistration: arav>, <staffregistration: arav>,]> like this so use next step given below
        
    #fetch_backenddata=staffregistration.objects.all()
    #return render(request,'home.html',{'fetched':  fetch_backenddata })    
        
    # refetchdata_4filter=staffregistration.objects.filter(first_name = "cristin")
    # return render(request,'home.html',{'fetched':  refetchdata_4filter })
    # this fetch data from your tables according the field name given in its attriubute like firs_name if available it will print & if Unavailble then display nothing
    # fetchdata_4get=staffregistration.objects.get(first_name = "rohan") ## this fetch data from your tables according the field name given in its attriubute like first_name if available it will print & 
    # #fetchdata_4get=staffregistration.objects.get(first_name = "cristin") #this name is unavalable it will through error {DoesNotExist at models table(/staffregistration) matching query does not exist.}
    # return render(request,'home.html',{'fetched':  fetchdata_4get })    

#not working signup
#def signup(request):
    try:
        if request.method == "POST":
            f_name=request.POST.get('firstname')
            l_name=request.POST.get('lastname')
            #age_=request.POST.get('sage')
            #mob_=request.POST.get('scontact')
            # email_=request.POST.get('email')
            # paswd_=request.POST.get('password')

            print(f_name,l_name)#,email_,paswd_,,age_,mob_

            # save_data=Staffregistration(
            #     first_name=f_name,
            #     last_name=l_name,
            #     age=age_,
            #     contact_no=mob_,
            #     email=email_,
            #     password=make_password(paswd_),
            # )
            # save_data.save()
            return render(request, 'career.html')
    except:
        return HttpResponse("Registration Successfull")


# def newsignup(request):
#     if request.method == "POST":
#         name=request.POST.get('firstname')
#         lname=request.POST.get('lastname')
#         print(name,lname)
#     else:
#         print("Post is not working")

#         return redirect('about')
    
    #return render(request,'about.html')

def login(request):
    aa =request.method == "POST"
    if aa:
        email_id=request.POST.get('lmail') #email ye input attribute ki name se a rha hai and store kr rha variable me comare krne ke liye models se
        pwd_=request.POST.get('lpwd') # same

        print(email_id,pwd_)

        try:
            fetch_email=User_resgistration.objects.get(email = email_id)
            #fetch_email=Staffregistration.objects.get(email = email_id) # yaha hum ye compare kr rhe hai, ki dali huyi shi haito hmare variable me save ho jaye jisse hum fir jo chahe vo field access kr skte hai
            if check_password(pwd_,fetch_email.password):  #yah pr hum chek kr rhe hai ki login ki huyi emai shi hai to password cke kre shi hai ya nhi
                #return HttpResponse("Login Successfully") # shi hai to ye dikhaye
                request.session['name']= fetch_email.first_name # ye hai log in ho gya to uska name dikhe or logout button dikhe session bad name mtlb isme store kr le or fir jaha vchahe vha request.session.name ke name dikha skte hai
                return redirect('home')
            else:
                return HttpResponse("Wrong Passsword") # shi nhi hai hai to ye dikhaye isiliye import kra hai  check_password or make password
        except:
            return HttpResponse("Email doesn't exist")
        
def logout(request):
    request.session.clear()
    return redirect('home')


def about(request):
    #return redirect('about.html')#it can not rediect to html by file name or
    #return redirect('about') # this can not directly redirect by its path name first you to render it
    return render(request,'about.html')


#to check redirect functionality it can only redirect those pages which is firstly render with request attributes

def career(reuquest):
    #return HttpResponseRedirect('career') # it also same as redirect first render then on other time can call by redirect or resposnse
    #return HttpResponseRedirect('about') # its worlks beacuse above this PAGE is RENDERED by REQUEST
    return render(reuquest,'career.html')

#this was for checking how its work
# def product(request):
#     # here we are bring id of category which is coming through {?category_id} from category div, which is showing product
#     cate_id=request.GET.get("category_id")
#     if cate_id:
#         product=Product.objects.filter(prod_category=cate_id)
#     else:
#         product=Product.objects.all()
#     # #fetcing the product data
#     # fetch_product=Product.objects.all()
#     # context={
#     #     'feproduct':fetch_product,
#     # }
#     # return render(request, "product.html", context=context)
#     return render(request, "product.html")


#new signup method all above not working miss happening with post method
def test(request):
    try:
        if request.method =='POST':
            # na=request.POST.get('namec')
            # la=request.POST.get('names')
            name=request.POST.get('sfname')
            lname=request.POST.get('slname')
            age_=request.POST.get('sage')
            contacts=request.POST.get('scontact')#,age_,contacts,emails,passwords
            emails=request.POST.get('semail')
            passwords=request.POST.get('spassword')
            print(name,lname)
            # print(na, la)
            print(age_,contacts)
            print(emails,passwords)
            save_dta=User_resgistration(
                first_name=name,
                last_name=lname,
                age=age_,
                contact_no=contacts,
                email=emails,
                password=make_password(passwords)
                )
            
            save_dta.save()
            
            return redirect('home')
            
    except:
        return HttpResponse("post not working")
    

#def test(request):
    #return render(request, 'testnghtml.html')