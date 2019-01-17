import geocoder
import requests


link="http://api.openweathermap.org/data/2.5/weather"

g = geocoder.ip('me')
g.latlng
print('your coordinates, city, country as follow:')
print(g.latlng)

print(g.city)
print(g.country)
value=g.city

additional_data = {}
additional_data["APPID"]="YOURAPIID"
additional_data["q"]=value
additional_data["units"]="metric"
g=additional_data
data = requests.get(link,params=additional_data).json()
print("------------------------------------------------------")
print(data)
print("------------------------------------------------------")
url='http://api.openweathermap.org/data/2.5/weather?appid=YOURAPIID&q=' + value
json_data = requests.get(url).json()
print('Weather description, wind speed, humidity:')

format_add = json_data['weather'][0]['description']
format_add1=json_data['weather'][0]['main']
format_add2=json_data['wind']['speed']
format_add3=json_data['main']['humidity']

print(format_add)
print(format_add1)
print(format_add2)
print(format_add3)

