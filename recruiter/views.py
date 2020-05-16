from django.shortcuts import render

# Create your views here.
from django.shortcuts import render




def thanks(request):
    return render(request, 'thanks.html')

def thankyou(request):
    return render(request, 'thankyou.html')



def register(request):
    return render(request, 'register.html')

def userinfoview(request):
    return render(request, 'info.html')
