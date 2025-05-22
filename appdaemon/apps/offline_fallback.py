import requests
import os

try:
    requests.get("http://homeassistant.local:8123", timeout=5)
except:
    os.system("curl -X POST http://192.168.1.25/cm?cmnd=Power%20On")
