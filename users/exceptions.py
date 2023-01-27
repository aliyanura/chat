from rest_framework.exceptions import APIException


class ObjectNotFoundException(APIException):
    status_code = 404