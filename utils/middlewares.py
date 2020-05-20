from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from utils.exc import AppException
# import logging
# logger = logging.getLogger('execution_time')


class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        def app_exception_handler():
            if exception.for_api:
                return JsonResponse(
                    dict(
                        type=type(exception).__name__,
                        code=exception.code,
                        message=exception.message
                    ),
                    status=exception.status
                )

        exception_handler = {
            AppException: app_exception_handler,
        }

        result = exception_handler.get(exception.__class__.__base__)
        return result() if result else None