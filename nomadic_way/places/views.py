from django.shortcuts import render
from django.http import HttpResponse


def sites(request):
    return HttpResponse("best sites to visit")


def site(request, pk):
    return HttpResponse("this site is one of its kind among top sites"+ ' ' +str(pk))