from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from gun_hubAppBackend.models import Product
# Create your views here.
def home_page(request):
   if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username = username, password = password)
           login(request, user)
           return redirect('/login')
   else:
       form = UserCreationForm()
   return render(request,'signInPage.html', {'form': form})

def mainPageView(request):
    all_product = Product.objects.all()
    context = {
        'products': all_product

    }
    return render(request, 'mainPage.html', context=context)


