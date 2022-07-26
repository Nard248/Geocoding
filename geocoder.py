import requests

API_KEY = 'AIzaSyBzyd4Z64TN7vCvvjGNlzMe8IXKNhrwVW8'

address = 'Armenia, Yerevan Komitas Str. 8'

params = {
    'key': API_KEY,
    'address': address
}

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
response = requests.get(base_url, params=params).json()
print(response)

if response['status'] == 'OK':
    geometry = response['results'][0]['geometry']
    lat = geometry['location']['lat']
    lng = geometry['location']['lng']
    print(lat, lng)
