from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.
def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "So Much Hate this month!!"
    elif month == "february":
        challenge_text = "A little Bit Hate!!"
    elif month == "march":
        challenge_text = "In love So much!!"
    else:
        return HttpResponseNotFound("Page Not Found!!")
    return HttpResponse(challenge_text)