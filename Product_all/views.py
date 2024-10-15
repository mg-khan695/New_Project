from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from Product_all.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user= authenticate(request, username=username, password=password)
        
        if user is not None:
            messages.error(request, 'Invalid username or password.')
            return redirect('/login/')
            # Redirect to a success page
        else:
            login(request, user)
            return redirect('/home/') 
        
    return render(request,'login.html')

def register_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')
        

        user=User.objects.create(
            username=username,
            first_name= first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save()
        messages.info(request,'Account Created Successfully')
        return redirect('/register/')

    return render(request,'register.html')

def logoutUser(request):
    logout(request)
    return redirect('/login/')

def product_page(request):
    product_name = None
    product_price = None
    product_image = None
    p_data= Product_add.objects.all()
    context= {'products':p_data}
    print(context)

    if request.method=='POST':
        data = request.POST
        product_name= data.get('product_name')
        product_price= data.get('product_price')
        category=data.get('category')
        product_image=request.FILES.get('product_image')
        
        if product_name and product_price:
            ptud=Product_add.objects.create(
                product_name=product_name,
                product_price=product_price,
                category=category,
                product_image=product_image
            )
            ptud.save()
            messages.success(request, 'Product added successfully!')
            return redirect('/product/')
        
    else:
            return render(request, 'product_all.html', {'error': 'Product name and price are required.'})

    return render(request,'homepage.html',context)

def delete_product(request, proId):
    obj=Product_add.objects.get(pk=proId)
    print(proId)
    obj.delete()
    return HttpResponseRedirect ('/home/')

@login_required(login_url="/login/")
def home_page(request):
    p_data= Product_add.objects.all()
    if request.method=="GET":
        ser=request.GET.get('search')
        if ser!=None:
            p_data=Product_add.objects.filter(product_name=ser)
    context= {'products':p_data}
    print(context)
    return render(request,'homepage.html', context)

def update_product(request, proId):
    update_data= Product_add.objects.get(pk=proId)

    if request.method=="POST":
        data=request.POST
        product_name=data.get('product_name')
        product_price=data.get('product_price')
        category=data.get('category')
        product_image=request.FILES.get('product_image')

        update_data.product_name=product_name
        update_data.product_price=product_price
        update_data.category=category

        if product_image:
            update_data.product_image=product_image

            update_data.save()
            messages.success(request, 'Updated Successfully')
            return redirect('/product/')
    context={'update_data':update_data}
    return render(request,'update_product.html',context)

def search_product(request):
    pro_data=Product_add.objects.all()
    if request.method=="GET":
        ser=request.Get.get('search')
        if ser!=None:
            pro_data=Product_add.objects.filter(product_name=ser)

    return render(request, 'home_page.html')

