import requests
import sys

try:
    resp = requests.get("https://database.company.com/devices/" + sys.argv[1] + "/allowedUsers" ,
                        timeout = 60)
    if resp.status_code == 200:
        users = resp.json()['allowedUsers']
        return " ".join(users)
except Exception as e:
    print "Unable to get response from remote site. Error : " + str(e)
    sys.exit(1)
