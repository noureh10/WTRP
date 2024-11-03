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

def get_vehicle():
	data = get_indicators()
	if data is not None :
		return (data["type"])
