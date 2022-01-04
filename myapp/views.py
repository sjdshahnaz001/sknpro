from django.shortcuts import render

# Create your views here.


def sad(request):
    return render(request,'sad.html')
