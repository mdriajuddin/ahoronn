from django.shortcuts import render
from .models import Pescription
from django.shortcuts import redirect
# Create your views here.
from django.views import View
from django.contrib import messages

def PescriptionCreateView(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        pescription = request.FILES['pescription']

        print(pescription)
        if [number, pescription] is not None:
            Pescription.objects.create(phone_number=number, image=pescription)
            return redirect('catalog:home')

