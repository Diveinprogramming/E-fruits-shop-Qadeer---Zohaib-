from django.shortcuts import render , redirect
from .models import Customer

def home(request):
 return render(request, 'app/home.html')

def product_detail(request):
 return render(request, 'app/productdetail.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def fruits(request):
 return render(request, 'app/fruits.html')

def vegetables(request):
 return render(request, 'app/vegetables.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
#  if not request.user.is_authenticated:
#         return redirect('')
        error = ""
        if request.method == "POST":
            email = request.POST['email']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']
            print(email)
        if password.null() or not email or not confirm_password:
            error = "empty"
        elif Customer.objects.filter(email=email) == True:
            error = "already"  
        else:
                

            try:
                Customer.objects.create(email=email, password=password)
                error = "no"
            except:
                error = "yes"
        return render(request, 'app/customerregistration.html', locals())

        
def checkout(request):
 return render(request, 'app/checkout.html')
