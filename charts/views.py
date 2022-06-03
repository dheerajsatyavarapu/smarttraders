from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def livetradeview(request):
    return render(request,"viewtrade.html")