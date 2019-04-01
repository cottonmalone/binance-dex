import requests
import urllib3
from .exceptions import generate_exception_for_code


def perform_request(request_fct, base_url, path, *args, **kwargs):
    """
    Perform given request and return JSON data from response.

    Args:
        request_fct (func): The function to use for the request (e.g
            requests.get)
        base_url (str): The base url of the host.
        path (str): The path of the API call.
        *args: Additional arguments for the request_fct.
        **kwargs: Additional keyword arguments for the request_fct.

    Returns:
        dict: JSON data from response.

    """

    # full url, merge base and path
    url = urllib3.util.Url(host=base_url, path=path)

    # send request and get the response
    response = request_fct(url, *args, **kwargs)

    # get the json data from the body
    data = response.json()

    # if status code is not OK, raise exception
    if response.status_code != requests.codes.ok:
        raise generate_exception_for_code(response.status_code, data['message'])

    return data


def get(base_url, path, *args, **kwargs):
    """
    Perform GET request and return JSON data from response.

    Args:
        base_url (str): The base url of the host.
        path (str): The path of the API call.
        *args: Additional arguments for the request_fct.
        **kwargs: Additional keyword arguments for the request_fct.

    Returns:
        dict: JSON data from response.

    """
    return perform_request(requests.get, base_url, path, *args, **kwargs)


def post(base_url, path, *args, **kwargs):
    """
    Perform POST request and return JSON data from response.

    Args:
        base_url (str): The base url of the host.
        path (str): The path of the API call.
        *args: Additional arguments for the request_fct.
        **kwargs: Additional keyword arguments for the request_fct.

    Returns:
        dict: JSON data from response.

    """
    return perform_request(requests.post, base_url, path, *args, **kwargs)
