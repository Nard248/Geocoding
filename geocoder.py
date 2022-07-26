import requests

API_KEY = 'AIzaSyBzyd4Z64TN7vCvvjGNlzMe8IXKNhrwVW8'

address = '1 hack drive, menlo park, CA'

params = {
    'key': API_KEY,
    'address': address
}

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
response = requests.get(base_url, params=params).json()
print(response)