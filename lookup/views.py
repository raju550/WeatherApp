from django.shortcuts import render


def home(request):
    import json
    import requests
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request: requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=71BC600B-FFD8-4FF6-99A8-36871C82A528")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        if api[0]['Category']['Name'] == "Good":
            category_description = "Air quality good for healthy"
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Air quality Moderate for healthy"
            category_color = "moderate"
        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})
    else:
        api_request: requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=71BC600B-FFD8-4FF6-99A8-36871C82A528")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error..."
        if api[0]["Category"]['Name'] == "Good":
            category_color = "good"
            category_description = "0 to 50	Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "Air quality Moderate for healthy"
            category_color = "moderate"

        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
