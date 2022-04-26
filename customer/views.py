from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.views.generic import ListView

# Create your views here.
@login_required
def Profile_View(request):

    return render(request, 'customer/profile.html')