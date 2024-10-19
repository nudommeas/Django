from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound ,HttpResponseRedirect
# Create your views here.
monthly_challenges = {
    "january": "Not in love with this",
    "february": "Almost My Bad Month",
    "march": "Make sure this month is Safe",
    "april": "What is fool day",
    "may": "Satisfacation",
    "june": "You can do it",
    "july": "Make it better than yesterday",
    "august":"better go to GYM",
    "october":"Nutrition",
    "september":"Best Luck",
    "november": "It is my BIRTHDAY!!"
}

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Page Not Found, Try again")

    redirect_month = months[month - 1]
    return HttpResponseRedirect(redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Page Not Found!")
    return HttpResponse(challenge_text)