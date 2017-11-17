import requests

r = requerst.get('http://apigithub.com/events')

print("Values \n", r.text)
print("CONTENT \n", r.content)
print("CODE \n", r.status_code)
print("JSON \n", r.json)

payload = {'key1':'value1', 'key2':'value2'}

r = requests.post("http://httpbin.org/post", data = payload)
print(r.text)

url = 'http://apigithub.com/event'
headers = {'user'}
