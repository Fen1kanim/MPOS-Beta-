import datetime
import os
import json
from subprocess import call

# opening databases
with open("keywords.json", "r") as jf:
    keywords = json.load(jf)

with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)

with open('./authentification/users.json', 'r') as js:
    users = json.load(js)
# opening authentification request
call(["python", "./authentification/request.py"])

# the main programm opens
print("print help to list comands")
print()

while True: # main cycle
    call(['python', './python/request.py'])
