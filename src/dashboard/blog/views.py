from .form import BlogForm
from front.models import Blog
from django.shortcuts import render, redirect


def blog_list(request):
    blog = Blog.objects.all()
    ctx = {
        "blogs": blog
    }
    return render(request, "dashboard/blog/list.html", ctx)


def blog_create(request):
    model = Blog()
    form = BlogForm(request.POST or None, instance=model)
    if request.POST:
        form.is_valid()
        form.save()
        return redirect("blog_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render("dashboard/blog/form.html", ctx)


def blog_edit(request, pk):
    model = Blog.objects.get(pk=pk)
    form = BlogForm(request.POST or None, instance=model)
    if request.POST:
        form.is_valid()
        form.save()
        return redirect("blog_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render("dashboard/blog/form.html", ctx)


def blog_delete(request, pk):
    model = Blog.objects.get(pk=pk)
    model.delete()
    return redirect("blog_list")
