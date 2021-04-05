from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def Index(request):
    return JsonResponse({'name': 'Arturo Negreiros'})