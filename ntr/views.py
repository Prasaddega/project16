from django.shortcuts import render

# Create your views here.

def temper(request):
    return render(request,'temper.html')

def aadhi(request):
    return render(request,'aadhi.html')