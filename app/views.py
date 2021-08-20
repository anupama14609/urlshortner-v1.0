from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import uuid
from .models import Url
from django.core import serializers
from django.views import View

def home(request):
    return render(request, 'app/home.html')

def Create(request):
    if request.method == 'POST':
        lnk = request.POST['link'] 
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link = lnk, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
             

def Go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)
