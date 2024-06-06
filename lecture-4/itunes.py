import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Incorrect number of arguments.")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])