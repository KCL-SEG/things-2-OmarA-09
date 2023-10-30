from django.shortcuts import render
from .forms import ThingForm

def home(request):
    form = ThingForm()
    # template 'form' which we assign to object :form
    return render(request, 'home.html', {'form': form})
