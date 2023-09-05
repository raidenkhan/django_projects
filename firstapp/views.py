from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature


# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = "Khortal"
    feature1.details = "Sevice is quick"
    feature1.isTrue = True

    feature2 = Feature()
    feature2.id = 2
    feature2.name = "Khano"
    feature2.details = "Sevice is hockck"
    feature2.isTrue = False

    feature3 = Feature()
    feature3.id = 3
    feature3.name = "Manueon"
    feature3.details = "lorem is some random thing"
    feature3.isTrue = True
    feature4 = Feature()
    feature4.id = 3
    feature4.name = "Something"
    feature4.details = "lol lorem"
    feature4.isTrue = True
    feature = [feature1, feature2, feature3, feature4]

    name = "Khortal"
    context = {"name": "Emmanuel", "age": 43, "nationality": "Ghana", "sex": "Male"}
    return render(
        request,
        "index.html",
        {"features": feature},
    )


# how do you send http response in django?
def counter(request):
    words = request.GET["words"]
    amount = len(words.split())
    return render(request, "counter.html", {"amount": amount})
