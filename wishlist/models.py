from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishlistItem(models.Model):
    """
    WishlistItem Model to add items to users wishlist
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='wishlist_items')
    # User who owns wishlist
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # Product added to wishlist
    added_at = models.DateTimeField(auto_now_add=True)
    # When review was created

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
