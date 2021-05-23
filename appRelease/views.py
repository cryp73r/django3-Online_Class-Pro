from django.http.response import HttpResponse
from .api_call_ver import apiCallVer

# Create your views here.
def apiv1Ver(request):
    return HttpResponse(apiCallVer(), content_type='application/json')