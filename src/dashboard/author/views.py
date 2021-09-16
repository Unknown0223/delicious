from django.shortcuts import render, redirect
from dashboard.author.form import AuthorsForm
from front.models import Author


def authors_create(request):
    model = Author()
    form = AuthorsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("authors_list")
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/authors/form.html', ctx)


def authors_list(request):
    authors = Author.objects.all()
    ctx = {
        'authors': authors
    }
    return render(request, 'dashboard/authors/list.html', ctx)

def authors_edit(request, pk):
    model = Author.objects.get(pk=pk)
    form = AuthorsForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("authors_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'dashboard/authors/form.html', ctx)


def authors_delete(request, pk):
    model = Author.objects.get(pk=pk)
    model.delete()
    return redirect("authors_list")