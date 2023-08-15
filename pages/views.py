from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices,fuel_choices, state_choices
from  listings.models import Listing
from seller.models import Seller

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices' : state_choices,
        'fuel_choices' : fuel_choices,
        'price_choices' : price_choices

    }
    return render(request, 'pages/index.html', context)

def about(request):
     # Get all sellers
    sellers = Seller.objects.order_by('-hire_date')

    # Get MVP
    mvp_sellers = Seller.objects.all().filter(is_mvp=True)

    context = {
        'sellers': sellers,
        'mvp_sellers': mvp_sellers
    }

    return render(request, 'pages/about.html', context)
