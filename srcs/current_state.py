import requests
import json

INDICATOR_WT_API = "http://localhost:8111/indicators"
MAP_IMAGE = "http://localhost:8111/map.img"

def get_indicators():
	response = requests.get(INDICATOR_WT_API)
	if response.status_code == 200:
		return response.json()
	else:
		return None

def get_map_img():
	response = requests.get(MAP_IMAGE)
	if  response.status_code == 200:
			return response
	else:
		return None

HANGAR_MSG = "Currently in the hangar"

def get_vehicle():
	data = get_indicators()
	map = get_map_img()
	if ((data is not None and map is None)):
		return (HANGAR_MSG)
	if ((data is not None and str(data["valid"]) == "True")):
		return (data["type"])