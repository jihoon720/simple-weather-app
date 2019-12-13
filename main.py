from credentials import API_KEY
import json, sys
import urllib.request

try:
	city = sys.argv[1]
	res = urllib.request.urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
	json = json.load(res)
	current_temp = json["main"]["temp"]
	temp_max = json["main"]["temp_max"]
	temp_min = json["main"]["temp_min"]
	print(f"Current temperature: {current_temp}")
	print(f"Temperature will be high as: {temp_max}")
	print(f"Temperature will be low as: {temp_min}")
except IndexError as e:
	print("Please type in city.")
