from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from recipes.utils import searchRecipes
from .models import Recipe
from .forms import RecipeForm
from .utils import paginateRecipes, searchRecipes


def recipes(request):

  recipes, search_query = searchRecipes(request)
  custom_range, recipes = paginateRecipes(request, recipes, 3)

  context = {'recipes':recipes,'search_query':search_query,'custom_range':custom_range}
  return render(request,'recipes/recipes.html',context)

    
def recipe(request, pk):
    recipeObj = Recipe.objects.get(id=pk)
    return render(request,'recipes/single-recipe.html',{'recipe': recipeObj})

@login_required(login_url="login")
def createRecipe(request):
  profile = request.user.profile
  form = RecipeForm()

  if request.method == 'POST':
    form = RecipeForm(request.POST,  request.FILES)
    if form.is_valid():
      recipe = form.save(commit=False)
      recipe.owner = profile
      recipe.save()
      return redirect('account')

  context = {'form': form}
  return render(request, "recipes/recipe_form.html",context)

@login_required(login_url="login")
def updateRecipe(request, pk):
  profile = request.user.profile
  recipe = profile.recipe_set.get(id=pk)
  recipe = Recipe.objects.get(id=pk)
  form = RecipeForm(instance=recipe)

  if request.method == 'POST':
    form = RecipeForm(request.POST, request.FILES, instance=recipe)
    if form.is_valid():
      form.save()
      return redirect('account')

  context = {'form': form}
  return render(request, "recipes/recipe_form.html",context)

@login_required(login_url="login")
def deleteRecipe(request, pk):
  profile = request.user.profile
  recipe = profile.recipe_set.get(id=pk)
  recipe = Recipe.objects.get(id=pk)
  if request.method == 'POST':
    recipe.delete()
    return redirect('account')
  context = {'object': recipe}
  return render(request, 'delete_template.html',context)