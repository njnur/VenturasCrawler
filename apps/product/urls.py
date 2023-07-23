from django.urls import path
from apps.product.api.v1.views import ProductView


urlpatterns = [
    path("products/", ProductView.as_view(), name='products'),
]
