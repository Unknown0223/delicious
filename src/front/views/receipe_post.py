from django.shortcuts import render

def recipes_post(request):
    return render(request, 'front/receipe-post.html')