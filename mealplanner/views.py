import requests
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Meal
from django.shortcuts import redirect, get_object_or_404

# Home Page
def home(request):
    return render(request, 'mealplanner/home.html')

def search_meals(request):
    query = request.GET.get('query', '')  # Get search query from the URL parameter
    if not query:
        return render(request, 'mealplanner/search_results.html', {'meals': []})

    # API URL with your query
    api_url = f"https://api.edamam.com/api/recipes/v2?type=public&q={query}&app_id={settings.EDAMAM_API_ID}&app_key={settings.EDAMAM_API_KEY}"

    # Add headers if required (example, you may need to use your user ID)
    headers = {
        'Edamam-Account-User': settings.EDAMAM_USER_ID  # Make sure to set this in settings.py
    }

    response = requests.get(api_url, headers=headers)
    
    # Log the response for debugging
    print(response.status_code)  # Check if the request was successful
    print(response.text)  # Log the raw response text

    if response.status_code == 200:
        meals = response.json().get('hits', [])
    else:
        meals = []

    return render(request, 'mealplanner/search_results.html', {'meals': meals})

# Save a meal to the user's meal plan
@login_required
def save_meal(request):
    if request.method == "POST":
        name = request.POST['name']
        image_url = request.POST['image_url']
        recipe_url = request.POST['recipe_url']

        Meal.objects.create(user=request.user, name=name, image_url=image_url, recipe_url=recipe_url)
        return redirect('saved_meals')

    return redirect('home')

# Show saved meals for logged-in users
@login_required
def saved_meals(request):
    # Get all saved meals for the logged-in user
    saved_meals = Meal.objects.filter(user=request.user)

    return render(request, 'mealplanner/saved_meals.html', {'saved_meals': saved_meals})
@login_required
def delete_meal(request, meal_id):
    # Get the meal object or return a 404 if not found
    meal = get_object_or_404(Meal, id=meal_id, user=request.user)
    
    # Delete the meal
    meal.delete()

    # Redirect back to the saved meals page
    return redirect('saved_meals')



# User signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'mealplanner/signup.html', {'form': form})
