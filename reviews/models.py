from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from products.models import Product


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)  # Link to the user who left the review
    rating = models.IntegerField(default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(
        default=timezone.now)  # Date the review was created

    def __str__(self):
        return (
            f"Review by {self.user.username} on "
            f"{self.created_at.strftime('%Y-%m-%d')}"
        )
