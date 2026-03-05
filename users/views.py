from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployeeCreationForm

def register_view(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = EmployeeCreationForm()
    return render(request, 'catalog/register.html', {'form': form})