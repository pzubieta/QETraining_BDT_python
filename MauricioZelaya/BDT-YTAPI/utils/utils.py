import requests

def get_conn(host, root_path, method, payload = None):
    """
    This method will set a get to a method.
    :param host: The host.
    :param root_path: The root_path.
    :param method: The method that will be tested.
    :param payload: Payload to send.
    :return: the response code
    """

    endpoint = host + root_path + method
    payload = payload
    request = requests.get(endpoint, payload)
    return request.status_code
