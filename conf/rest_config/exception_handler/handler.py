from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    Call REST framework's default exception handler first,
    to get the standard error response.
    """
    response = exception_handler(exc, context)

    """
    Update the structure of the response data.
    """
    if response is not None:
        customized_response = {'errors': []}
        if isinstance(response.data, dict):
            for key, value in response.data.items():
                if isinstance(value, list) and len(value) > 0:
                    value = value[0]
                error = {'field': key, 'message': value}
                customized_response['errors'].append(error)
        elif isinstance(response.data, list):
            error = {'field': 'detail', 'message': response.data[0]}
            customized_response['errors'].append(error)
        response.data = customized_response
    return response
