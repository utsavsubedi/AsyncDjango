from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_function
from django.http import HttpResponse

# Create your views here.
def test(request):
    test_function.delay()
    return HttpResponse('Hello World')