import requests

custom_headers = {
    "Accept-language": "en-GB,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
}

url = "https://www.amazon.com/SAMSUNG-Border-Less-Compatible-Adjustable-LS24AG302NNXZA/dp/B096N2MV3H?ref_=Oct_DLandingS_D_fe3953dd_2"

response = requests.get(url, headers=custom_headers)

with open('with_captcha.html', 'w') as file:
    file.write(response.text)