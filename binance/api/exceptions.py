
class APIException(Exception):
    """
    Generic exception class for the api module.
    """
    pass


class BadRequest(APIException):
    """
    Exception for when the server rejects the request due to malformed input.
    """
    pass


class NotFound(APIException):
    """
    Exception for when the requested resource could not be found.
    """
    pass


class UnknownError(APIException):
    """
    Exception for when the returned error is not known.
    """
    pass


ERROR_CODES_TO_EXCEPTION = {
    400: BadRequest,
    404: NotFound
}
"""
Map error codes to associated exceptions.
"""


def generate_exception_for_code(code, message):
    """
    Generate exception for given status code.

    Args:
        code (int): The HTML code from the response.
        message (str): The error message.

    Returns:
        Exception: The correct exception for the given status code and message.

    """
    # get correct exception type
    exception_type = ERROR_CODES_TO_EXCEPTION.get(code, UnknownError)

    return exception_type(message)
