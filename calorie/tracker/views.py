from django.shortcuts import render
from .secrets import Nutrition_Key

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        query = request.POST['query']
        api_url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        headers = {
            'x-app-id': 'f39c08df',  # Replace with your actual App ID
            'x-app-key': Nutrition_Key,
            'Content-Type': 'application/json'
        }
        body = {
            "query": query,
            "timezone": "US/Eastern"  # You can adjust the timezone as needed
        }

        try:
            api_request = requests.post(api_url, headers=headers, json=body)
            api_request.raise_for_status()  # Raise an HTTPError for bad responses
            api = api_request.json()
            print(api)
        except requests.exceptions.RequestException as e:
            api = "Oops! There was an error: {}".format(e)
            print(e)

        return render(request, 'home.html', {'api': api})
    else:
        return render(request, "home.html", {'query': "Enter a valid query"})
