from rest_framework import status
from rest_framework.exceptions import APIException


class DefaultServerError(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "There is a problem on server."
    default_code = 'default server error'
