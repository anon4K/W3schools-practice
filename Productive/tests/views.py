from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import TestModel
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({'status': 'ok'})

def test_view(request):
    mymembers = TestModel.objects.all().values()
    template = loader.get_template('all_tests.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context,request))

def more(request):
    template = loader.get_template('further.html')
    return HttpResponse(template.render({}, request))

def details(request, id):
    mymember = TestModel.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = TestModel.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

