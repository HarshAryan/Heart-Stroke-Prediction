from random import randint
from django.http import JsonResponse

def predict(request):
    n = randint(50, 80)
    if request.method == "POST":    
        return JsonResponse({"results":n },safe=False)
    else:
        return JsonResponse(["This url is POST only"],status=400)
