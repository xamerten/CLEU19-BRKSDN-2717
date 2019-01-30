# Test Room:  Y2lzY29zcGFyazovL3VzL1JPT00vYWI0MjhiNjAtMTdlNy0xMWU5LWExODktODUzZGU1YzMyNzZm
# Prod Room:  Y2lzY29zcGFyazovL3VzL1JPT00vZjIxZTRkZTAtMTdlNi0xMWU5LWFmMzUtZjNjOWM5ZmE0N2Ji
import json
import os
import sys

import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt.multipart.encoder import MultipartEncoder

proxies = {
    'http': 'http://proxy.esl.cisco.com:8080',
    'https': 'http://proxy.esl.cisco.com:8080',
}

SPARK_ACCESS_TOKEN = "NzZkM2FjODgtZmI1Mi00ZWM5LWFmMzItMGQ4MDQ1NDM4MTllN2Q4NzhiMWUtNzFm_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
SPARK_ROOM_ID = "Y2lzY29zcGFyazovL3VzL1JPT00vYWI0MjhiNjAtMTdlNy0xMWU5LWExODktODUzZGU1YzMyNzZm"

# Disable Certificate warning
try:
    requests.packages.urllib3.disable_warnings()
except:
    pass

session = requests.Session()
session.proxies = proxies

# Get the absolute path for the directory where this file is located "here" for sending a file
here = os.path.abspath(os.path.dirname(__file__))

jsonstring = MultipartEncoder({'roomId': SPARK_ROOM_ID, 'text': 'A new Developer CI/CD build just finished!'})
message = session.post('https://api.ciscospark.com/v1/messages', data=jsonstring,
                       headers={'Authorization': 'Bearer ' + SPARK_ACCESS_TOKEN,
                       'Content-Type': jsonstring.content_type})

print(message)
