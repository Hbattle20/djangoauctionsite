from django.shortcuts import render
from django.http import HttpResponse

# probably need a user homepage
# homepage for all auctions
# the specific auction page for 1 auction
# maybe something for admins 

def siteHomepage(request):
    return HttpResponse("site homepage")


def user_homepage(request):
    return HttpResponse("user_homepage")


def singleStorageUnit(request):
    return HttpResponse("unit ID: xyz")


