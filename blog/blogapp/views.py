# from django.shortcuts import render,HttpResponse,redirect
# from blogapp.models import basemax

from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

  
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        
        if password1==password2:        
            user=User.objects.create_user(username=username,email=email,password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(request,'Your account has been created! You are able to login')
            return redirect('Login')
        else:
            messages.warning(request,'Password Mismatching...!!!')
            return redirect('remo')        
    else:
        form=CreateUserForm()        
        return render(request,"remo.html",{'form':form})
    
        
        # 
        # if password1==password2:
            # user = User.objects.create_user(username=username,email=email,password=password1)
            # user.is_staff=True
            # user.is_superuser=True
            # user.save()
        #    
        #    
            # messages.success(request, 'Form submitted successfully!')
            # return redirect('login')  # Redirect to a success page
        # else:
        #   messages.warning(request,'Password Wrong...!!')
        #   return redirect('remo')
    # else:
        # form = CreateUserForm()
        # return render(request, 'register.html', {'form': form})
# 
# 



@login_required(login_url='remo')
def profile(request):
    return render(request,'profile.html')
    



def logout(request):
    return render(request,'logout.html')
    















