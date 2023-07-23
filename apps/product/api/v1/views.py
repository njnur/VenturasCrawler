from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class ProductView(APIView):
    """
    A simple API for viewing and the products
    """
    Response(
        {
            "message": "Data Retrieved Sucessfully!"
        },
        status=HTTP_200_OK
    )
