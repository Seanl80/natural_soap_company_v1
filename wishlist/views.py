from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import WishlistItem

@login_required
def wishlist(request):
    """
    A view to render the user's wishlist
    """
    wishlist_items = WishlistItem.objects.filter(user=request.user)

    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product from the store to the
    wishlist after login
    """
    product = get_object_or_404(Product, pk=product_id)

    # Check if the product is already in the wishlist
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    
    if created:
        messages.info(request, "A new product was added to your wishlist")
    else:
        messages.info(request, "This product is already in your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the store to the
    wishlist after login
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = WishlistItem.objects.filter(user=request.user, product=product)

    if wishlist_item.exists():
        wishlist_item.delete()
        messages.info(request, "A product was removed from your wishlist")
    else:
        messages.info(request, "This product was not in your wishlist")

    return redirect(request.META.get('HTTP_REFERER'))
