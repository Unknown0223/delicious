from django.shortcuts import render

def recipes(request):
    return render(request, 'front/receipes.html')