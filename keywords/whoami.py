import json 

def whoami():
    with open('./authentification/lastUser.json', 'r') as js:
        lastUser = json.load(js)
    print('you are as', lastUser["name"], 'authorized')
