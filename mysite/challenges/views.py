
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

monthly_challenges = {
    "january": "So Much Hate this month!!",
    "february": "A Littke Bit Hate!!",
    "march": "In Love So much!!",
    "april": "Literaly, Love It!!",
    "may": "Adorable",
    "june": "Stunning",
    "july": "Hit me up Tonight",
    "august": "It's time to release my potential",
}
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Page Not Found, Try again")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenges_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Page Not Found!!!")

    return HttpResponse(challenges_text)