from random import choice
from django.http import HttpResponse

def index(request):
    omikuji = ["凶","吉","中吉","大吉"]
    result = choice(omikuji)
    response = HttpResponse(result)
    return response
