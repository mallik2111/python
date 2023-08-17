import requests
import json
import sys

if len(sys.argv) < 2:
    sys.exit("Need a file name")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
response1 = requests.get("https://10.234.137.158/api/mo/sys/intf/phys-[eth1/1].json?rsp-subtree=full")

o = response.json()
for result in o['results']:
    print(result["trackName"])
print(json.dumps(response1.json(), indent =2))
