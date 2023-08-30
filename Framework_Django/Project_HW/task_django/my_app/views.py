from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'my_app/about.html')


def about(request):
    return render(request, 'my_app/index.html')
