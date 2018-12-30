# this repository is an example of fetching information from URL and posting it into a steem post
from steem import Steem
import urllib.request
import json
import random
import json

chibi_number = random.randint(1, 850)
chibi = urllib.request.urlopen('https://chibigame.io/chibis.php?g&idj=' + str(chibi_number))
result = chibi.read()
result_json = json.loads(result)

chibi_name = (result_json["name"])
avatar = (result_json["imageUrl"])
description = (result_json["description"])

print ("fetching chibi name..." + chibi_name)
print ("fetching avatar URL... " + avatar)
print ("fetching description..." + description)
print ("posting to Steemit.com")

s = Steem(keys=["YOUR PRIV KEY"])
s.commit.post(
    "Daily Chibi: {}".format(chibi_name),
    "**{}**".format(chibi_name) + "<br> {}".format(avatar) + "<br>**Description:** {}<br>".format(description) + "<br>*This post was posted by the [Daily Chibi Poster](https://github.com/PixelNoob/python-steem)* <br>",
    "YOUR ACCOUNT",
    tags=["game","chibifighter", "chibigame"]
)
print ("your Chibi has been posted succesfully")
