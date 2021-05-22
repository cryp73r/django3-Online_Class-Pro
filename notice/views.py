from classdetail.api_call_cs import apiCallCS
from django.shortcuts import render
from django.http.response import HttpResponse
from .api_call import apiCall

# Create your views here.
def notices(request):
    return HttpResponse(apiCall(), content_type='application/json')