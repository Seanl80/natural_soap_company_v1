from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/add/', views.add_review, name='add_review'),
    path('product/<int:product_id>/', views.product_reviews, name='product_reviews'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),

]
