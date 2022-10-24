from django.shortcuts import render,redirect
from .forms import registerUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout 
# Sign Up Form
def signUp(request):
    if request.method == 'POST':
        form = registerUser(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            return redirect('signin')
    else:
        form = registerUser()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

# Sign in Form
def signIn(request):
    if request.method == 'POST':
       form =  AuthenticationForm(request=request,data=request.POST)
       if form.is_valid():
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=username,password=password)
           if user is not None:
               login(request,user)
               return redirect('home-page')
    #    else:
    #     print(form.errors)  for debugging      
    else:
       form =  AuthenticationForm()            
    context = {
        'form':form
    }
    return render(request, 'accounts/signin.html', context) 