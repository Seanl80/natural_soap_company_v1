from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from products.models import Product
from .forms import ReviewForm

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form, 'product': product})

def product_reviews(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()
    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews})
    
