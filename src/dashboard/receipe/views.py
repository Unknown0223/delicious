from django.shortcuts import render, redirect
from front.models import Recipe
from .form import RecipeForm


def recipe_create(request):
    model = Recipe()
    form = RecipeForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    ctx = {
        'model': model,
        'form': form,
    }
    return render(request, "dashboard/recipes/form.html", ctx)


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, "dashboard/recipes/list.html", ctx)


def recipe_edit(request, pk):
    model = Recipe.objects.get(pk=pk)
    form = RecipeForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            model.image = request.POST.get("image")
            form.save()
            return redirect('recipe_list')
    ctx = {
        'model': model,
        'form': form
    }
    return render(request, 'dashboard/recipes/form.html', ctx)


def recipe_delete(request, pk):
    model = Recipe.objects.get(pk=pk)
    model.delete()
    return redirect("recipe_list")
