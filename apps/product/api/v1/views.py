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

        return Response({"message": "Data retrieved"}, status=HTTP_200_OK)
