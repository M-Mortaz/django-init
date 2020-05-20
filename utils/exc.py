class AppException(Exception):
    code = 0
    message = ''
    status = 0
    extra = dict()

    def __init__(self, for_api=True, message='', status=0, **kwargs):
        self.for_api = for_api
        if message:
            self.message = message
        if status:
            self.status = status
        if kwargs:
            self.extra = kwargs
        self.set_complex_message()

    def set_complex_message(self):
        pass

    def __str__(self):
        return '{}-{}'.format(self.code, self.message)


class FileNotExistsInRequest(AppException):
    code = 2000
    message = "There is not file in request"
    status = 400


class InputMethodNotAllowException(AppException):
    code = 2001
    message = "The input method not allow yet"
    status = 400


class CustomMessageException(AppException):
    code = 2002
    status = 422

    def set_complex_message(self):
        self.message = f"{self.extra.get('custom_message')}"
