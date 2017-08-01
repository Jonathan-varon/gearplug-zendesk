from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def zendesk_webhook(request):
    print(request.GET)
    print(request.POST)
    print(request.body)
    return render(request,'webhook.html')
# Create your views here.


