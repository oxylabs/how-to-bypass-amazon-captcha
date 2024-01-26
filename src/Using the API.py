import requests
from pprint import pprint


payload = {
    'source': 'amazon',
    'url': 'https://www.amazon.com/dp/B096N2MV3H',
    'parse': True
}

response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('username', 'password'),
    json=payload,
)


pprint(response.json())

with open('without_captcha.json', 'w') as file:
    file.write(response.text)