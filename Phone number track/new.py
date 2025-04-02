import phonenumbers 
from phonenumbers import geocoder
from test import number
import folium
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


Key = "your api key"
#Phonenumber Location
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number,"en")
print(number_location)

#Service provider
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))


geocoder = OpenCageGeocode(Key)

query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

#map function
map_location = folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
