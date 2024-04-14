import requests

url = 'http://localhost:8000/api/v1/cc/'
url = 'http://localhost:8000/api/v1/up/'
data = {
    # 'Country_id' : ''
    'country_name' : 'India',
    'country_code' : 'IN',
    'description' : 'Proud',
    'logo_url' : 'https://flagsapi.com/IN/flat/64.png',
    'status': 'bool'

}

response = requests.post(url, data=data)
print(response.status_code)  # Check response status code
print(response.json())       # Print response data
