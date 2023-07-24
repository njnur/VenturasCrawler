from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_404_NOT_FOUND

from apps.product.models import Product
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class HomeView(APIView):
    @staticmethod
    def get(request):
        return Response({
            'message': 'Welcome to Venturas Crawler!!'
        },
            status=HTTP_200_OK
        )


class ProductView(APIView):
    """
    API for searching product using 'jan' value
    """
    @staticmethod
    @swagger_auto_schema(
        operation_description="Search product using JAN code", manual_parameters=[
            openapi.Parameter('jan', openapi.IN_QUERY, "JAN code", type=openapi.TYPE_STRING)],
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "data": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "jan": openapi.Schema(type=openapi.TYPE_STRING),
                            "product_name": openapi.Schema(type=openapi.TYPE_STRING),
                            "attributes": openapi.Schema(type=openapi.TYPE_STRING),
                            "maker": openapi.Schema(type=openapi.TYPE_STRING),
                            "brand": openapi.Schema(type=openapi.TYPE_STRING),
                            "tags_from_description": openapi.Schema(type=openapi.TYPE_STRING),
                            "tags_from_review": openapi.Schema(type=openapi.TYPE_STRING),
                        },
                    ),
                },
            ),
        },
    )
    def get(request):
        jan_code = request.query_params.get('jan')
        if not jan_code:
            return Response({"message": "Invalid query param"}, status=HTTP_422_UNPROCESSABLE_ENTITY)

        product = Product.objects.filter(jan=jan_code).first()
        if not product:
            return Response({"message": "Invalid JAN code"}, status=HTTP_404_NOT_FOUND)

        return Response({"message": "Data retrieved",
                         "data": {
                              "jan": product.jan,
                              "product_name": product.product_name,
                              "attributes": product.attributes,
                              "maker": product.maker,
                              "brand": product.brand,
                              "tags_from_description": product.jan,
                              "tags_from_review": product.jan,
                          }}, status=HTTP_200_OK)


class ReportView(APIView):
    """
    API for report creation according to the business logic
    """
    @staticmethod
    def get(request):
        total_product_count = Product.objects.count()
        product_name_count = Product.objects.exclude(product_name__isnull=True).exclude(product_name__exact='').count()
        attributes_count = Product.objects.exclude(attributes__isnull=True).exclude(attributes__exact='').\
            exclude(attributes__exact=[]).count()
        maker_count = Product.objects.exclude(maker__isnull=True).exclude(maker__exact='').count()
        brand_count = Product.objects.exclude(brand__isnull=True).exclude(brand__exact='').count()
        tags_from_description_count = Product.objects.exclude(tags_from_description__len__gt=0).count()
        tags_from_review_count = Product.objects.exclude(tags_from_review__len__gt=0).count()

        return Response({"message": "Data retrieved for fulfillment rate",
                         "data": {
                             "product_name": round((product_name_count/total_product_count), 4),
                             "attributes": round(attributes_count/total_product_count, 4),
                             "maker": round(maker_count/total_product_count, 4),
                             "brand": round(brand_count/total_product_count, 4),
                             "tags_from_description": round(tags_from_description_count/total_product_count, 4),
                             "tags_from_review": round(tags_from_review_count/total_product_count, 4),
                         }}, status=HTTP_200_OK)
