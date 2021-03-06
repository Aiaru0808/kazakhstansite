from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'posts/index.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponse("<h1>Registration successfuly done!</h1>")
    else:
        form = RegistrationForm()
        return render(request, 'posts/registration.html', {'form': form})