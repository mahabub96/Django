from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to the login page after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})



def custom_logout(request):
    if request.method == "POST":  # Only log out on a POST request for security
        logout(request)
        return redirect(reverse('login'))  # Redirects to login page after logout
    return render(request, 'logout.html') 
