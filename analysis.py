import requests
import re
import json

def extract_server_name(response :str):
    match = re.search(r'Server ID: (\w+)', response)
    if match:
        return match.group(1)
    else:
        return None

url = 'http://127.0.0.1:8000/home'

server_count = {}
for i in range(1000):

    response = requests.get(url)
    print(response.text)
    server_name = extract_server_name(response.text)

    if server_name:
        if server_name in server_count.keys():
            server_count[server_name] += 1
        else:
            server_count[server_name] = 1

print(server_count)