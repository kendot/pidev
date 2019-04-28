import os
import sys
import time
import pprint
import requests

BASE_URL = 'https://api-test03.cbdtest.io'
AUTH = os.environ['CBD_API_KEY']

s = requests.Session()
s.headers = {'X-AUTH-TOKEN': AUTH, 'Content-Type': 'application/json'}

try:
	data = s.get(BASE_URL + '/integrationServices/v3/device').json()
except requests.exceptions.ConnectionError as e:
	sys.exit(f'Error retrieving data from {BASE_URL}:\n{e}')

for device in data['results']:
	if 'internal' in device['name'] or 'DEREGISTERED' in device['status']:
		pass
	else:
		if (int(time.time()) - int(device['lastContact']/1000)) > 86400:
			print('Device {} ({}) has not checked in with 24 hours'.format(
				device['name'], device['deviceId']))
		
