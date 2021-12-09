from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["Cherries", "Apples", "Orange", "Strawberries", 'Pears', 'Watermelons']
    context = {
        'products': products,
    }
    return render(request, "home.html", context)

# from django.http import HttpResponse
#
#
# def home(request):
#     user = request.user
#     return HttpResponse("<h1>Welcome {}.</h1>".format(user))
