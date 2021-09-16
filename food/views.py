from django.shortcuts import render

def home_page(request):
    return render(request, "food/index.html")

def contact_page(request):
    return render(request, 'food/contact.html')

def blog_page(request):
    return render(request, 'food/blog-post.html')