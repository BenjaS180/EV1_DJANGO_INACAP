from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'campeones.html')

def prueba(request):
    return render(request,'html.html')