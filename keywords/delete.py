import json

with open('./authentification/lastUser.json', 'r') as js:
    lastUser = json.load(js)
with open('./authentification/users.json', 'r') as js:
    users = json.load(js)

stdin = input("type your password: ")

if stdin == users[lastUser["name"]]["password"]:
    del users[lastUser["name"]]
else:
    print("wrong password")

with open('./authentification/users.json', 'w') as js:
    json.dump(users, js, indent = 4)
