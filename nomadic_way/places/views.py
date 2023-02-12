from django.shortcuts import render
from django.http import HttpResponse


def sites(request):
    return render(request,'places.html')


def site(request, pk):
    return render(request,'single-site.html')