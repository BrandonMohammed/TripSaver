from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import InputForm

def home(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            destination = form.cleaned_data.get('destination')
            distance = form.cleaned_data.get('distance')
            return redirect('UPC-home')
    else:
        form = InputForm()
        return render(request, 'UberPriceCheck/homepage.html', {'form': form})
