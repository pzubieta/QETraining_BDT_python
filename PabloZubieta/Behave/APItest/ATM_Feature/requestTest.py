import requests

r = requerst.get('http://apigithub.com/events')

print("Values \n", r.text)
print("CONTENT \n", r.content)
print("CODE \n", r.status_code)