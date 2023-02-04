from django.shortcuts import render

from .models import Listing


def index(request):
    context = {
        'listings': Listing.objects.all()
    }
    return render(request, 'listings/listings.html', context=context)


def listings(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
