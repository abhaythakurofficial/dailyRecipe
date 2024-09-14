from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")

def index(request):
    if request.method == "POST":
        food_name = request.POST.get("food_name")
        food_img = request.FILES.get("food_img")

        # Save data to the Food model in the recipe app
        Food.objects.create(
            name=food_name,
            image=food_img,
        )
        return redirect('/recipe/')  # Redirect to prevent form resubmission
    
    queryset = Food.objects.all()
    if request.GET.get("search"):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'recipe': queryset}
    
    return render(request, "food/index.html", context)

def delete_recipe(request, id):
    queryset = Food.objects.get(id=id)
    queryset.delete()
    return redirect('/recipe/')  # Redirect to prevent form resubmission

def update_recipe(request, id):
    queryset = Food.objects.get(id=id)
    if request.method == "POST":
        food_name = request.POST.get("food_name")
        food_img = request.FILES.get("food_img")

        if food_img:
            queryset.image = food_img
        queryset.name = food_name

        queryset.save()
        return redirect('/recipe/')

    context = {'recipe': queryset}
    return render(request, "food/update.html", context)

def register(request):
    if request.method == "POST":
        email = request.POST.get("user_email")
        password = request.POST.get("user_password")

        if not User.objects.filter(email=email).exists():
            user = User.objects.create(
                username=email,  
                email=email,
            )
            user.set_password(password)  
            user.save()
            messages.info(request, "Account created successfully")
        else:
            messages.error(request, "Email already exists")
    
            return redirect('/register/')  
    return render(request, "food/register.html")

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("user_email")
        password = request.POST.get("user_password")

        if not User.objects.filter(email=email).exists():
            messages.info(request, "Invalid User email")
            return redirect('/login/')  
        user = authenticate(username=email, password=password)

        if user==None:
            messages.error(request, "Invalid password")
            return redirect("/login/")

        else:
            login(request,user)
            return redirect("/recipe/")

    return render(request, "food/login.html")

def logout_page(request):
    logout(request)
    return redirect("/login/")
