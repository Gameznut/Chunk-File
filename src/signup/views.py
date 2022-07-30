from cmath import log
from django.shortcuts import redirect, render
from .form import RegisterForm, LoginForm
from django.contrib import messages
# Create your views here.
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
 
# Views
def home_view(request,*args, **kwargs):

    context = {}
    return render(request, "home.html", context)


def signup_create_views(request):
    
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'signup.html', context)
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('home')
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'signup.html', context)
            
    return render(request, 'signup.html', {})

# def login_view(request): 
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(password)
#         if user is not None:
#             print("not")
#             login(request, user)
#             return redirect('home')
#         else:
#             print("one")
#             messages.success(request, 'Error while logging in')
#             return redirect('login')
#     else:
#         print("two")
#         return render(request, 'login.html', {})