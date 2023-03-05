from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello world!")
    # Create your views here.


def login(request):
    if request.method == 'POST':
       name = request.POST['user']
    
       pass1 = request.POST['pass']
       print(name,pass1 +"this usr name and password" )

       user=authenticate(username=name,password=pass1)
       
       if user is not None:
            
            print('Welcome')
           
      
            return redirect('dash')
       else:
            print('Login failed')
         
          
            return redirect('login')

   
    
    return render(request,'home.html')

def fail(request):
  template = loader.get_template('fail.html')
  return HttpResponse(template.render())

def reg(request):
    if request.method == 'POST':
        #username = request.POST("email")
        username = request.POST['email']
        password = request.POST['psw']

        db=User.objects.create_user(username,password)

        db.save()
        

        return redirect('login')

   
    return render(request,'reg.html')

def dash(request):
  template = loader.get_template('dash.html')
  return HttpResponse(template.render())