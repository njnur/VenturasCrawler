from django.urls import path
from apps.product.api.v1.views import ProductView, ReportView, HomeView


urlpatterns = [
    path("products/", ProductView.as_view(), name='products'),
    path("reports/", ReportView.as_view(), name='reports'),
    path('', HomeView.as_view(), name="home")
]
