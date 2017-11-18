import requests

def get_conn(host, root_path, method, payload = None):
    """
    this method will request a get and return the status code
    :param host: the host
    :param root_path: the rootpath of the url
    :param method: the method that will me test
    :param key: API key of the user
    :param snippet: optional param for some methods
    :return: the status code
    """
    endpoint = host + root_path + method
    payload = payload
    request = requests.get(endpoint, payload)
    return request.status_code
