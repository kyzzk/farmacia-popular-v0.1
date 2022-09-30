from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm


def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)

            return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)

def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')
