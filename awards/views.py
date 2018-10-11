from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
# Create your views here.
def award(request):
    return render(request,'index.html')