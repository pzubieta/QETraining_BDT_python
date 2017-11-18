import requests


def getConnection(host, rootPath):
    endpoint = host+rootPath+"/comments"
    r = requests.get(endpoint)
    return r.status_code
