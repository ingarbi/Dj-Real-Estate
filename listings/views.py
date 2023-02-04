from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Listing


def index(request):
    listings = Listing.objects.select_related('realtor').order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context=context)


def listings(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
