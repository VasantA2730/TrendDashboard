from django.shortcuts import render
from rest_framework.decorators import api_view
from .dictionary import get_dictionary
from django.http import JsonResponse
# Create your views here.

@api_view(['GET'])
def get_data(request):
    data = get_dictionary()

    return JsonResponse(data)