from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    json = [
        {
            'message':'Hello World!'
        }
    ]
    return JsonResponse({'json' : json})