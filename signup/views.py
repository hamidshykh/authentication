from django.shortcuts import redirect , render 
from django.http import HttpResponse , HttpRequest
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login

def signup(request):

    if request.method == 'POST':
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact_number = request.POST['cnumber']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if len(contact_number) != 11 :
            messages.error(request,'Number Should Be 11 Digit') 
            return redirect ('/signup')
        elif password != confirm_password:
            messages.error(request,'Password And Confirm Password Do Not Match')
            return redirect('/signup')
        else:
            user = User.objects.create(username=email , email = email , password = confirm_password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,'Your Account Successfully Created')
            return redirect('/login')


    return render(request , 'signup.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email , password=password)
        print (user)
        if user is not None:
            auth_login(request, user)
            messages.success(request , 'Successfully Login')
            return redirect('/signup')
        else:
            messages.error(request,'Something Went Worng')
            return redirect (request,'/login')

    return render(request , 'login.html')