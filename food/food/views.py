from django.shortcuts import render, redirect
from recipe.models import Food  
from django.http import HttpResponse
from recipe.models import Food

def index(request):
    recipe=Food.objects.all()
    context={'recipe':recipe}
    return render(request, "index.html",context)
