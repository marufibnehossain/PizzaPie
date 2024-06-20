from django.shortcuts import render, redirect
from django.http import HttpResponse
import pyrebase
import json
from django.contrib import messages


config = {
    "apiKey": "AIzaSyDmvnYBCzyksnycrqJOXVlfYrUI8-SE3qc",
    "authDomain": "pizzapie-e0799.firebaseapp.com",
    "databaseURL": "https://pizzapie-e0799.firebaseio.com",
    "projectId": "pizzapie-e0799",
    "storageBucket": "pizzapie-e0799.appspot.com",
    "messagingSenderId": "757989005591",
    "appId": "1:757989005591:web:8995d12495d8d90a7cbf52",
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
database=firebase.database()

# Create your views here.
def index(request):
    # foodname= database.child('food_data').child('foodname').get().val()
    # price= database.child('food_data').child('price').get().val()
    # desc= database.child('food_data').child('desc').get().val()
    return render(request, 'index.html', {
        # "foodname":foodname,
        # "price":price,
        # "desc":desc,
    })

def login_page(request):
    return render(request, 'login.html', {})

def postsign(request):
    email=request.POST.get("email")
    passw=request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email, passw)
        return render(request, "index.html", {"email": email})
    except requests.exceptions.HTTPError as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        messages.error(request, error)
        return redirect('login')

def register_page(request):
    return render(request ,'signup.html', {})
