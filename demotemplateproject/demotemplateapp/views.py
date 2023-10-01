from django.http import HttpResponse
from django.shortcuts import render
from .models import django,place
# Create your views here.
def demo(request):
    result=django.objects.all()
    output = place.objects.all()
    return render(request,"index.html",{'key':result,'key1':output})

