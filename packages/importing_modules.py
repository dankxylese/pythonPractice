import requests

r = requests.get("http://www.slapmywang.com")

print(r, type(r))

print(r.status_code)
print(r.content)
