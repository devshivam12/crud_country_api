import requests

url = 'http://localhost:8000/api/v1/cc/'
url = 'http://localhost:8000/api/v1/up/'
data = {
    'country_name' : 'India',
    'country_code' : 'IN',

}

response = requests.post(url, data=data)
print(response.status_code) 
print(response.json())       
