from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.shortcuts import render, redirect # type: ignore

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, 'accounts/login.html', context=context)
        
        login(request, user)
        return redirect('/')

    return render(request, 'accounts/login.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')
    
    return render(request, 'accounts/logout.html', {})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login/')
    
    context = {
        "form": form
    }
    
    return render(request, "accounts/register.html", context=context)