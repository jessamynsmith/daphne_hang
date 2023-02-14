import requests
from django.http import JsonResponse


def good(request):
    return JsonResponse({'message': 'good'})


def hang(request):
    res = requests.get(f"http://127.0.0.1:5000/api/v1/hang/")
    return JsonResponse(res.json())
