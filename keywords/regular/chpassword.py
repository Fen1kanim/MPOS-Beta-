import json

def chpassword(name):
    with open("./auth/users.json", "r") as js:
        users = json.load(js)

    oldPass = input("type your last pass: ")

    if oldPass == users[name]["password"]:
        pass
    else:
        return "0"

    sure = input("r u sure?(y/n): ")
    if sure == "y":
        users[name]['password'] = input("type ur new pass: ")
        with open("./auth/users.json", 'w') as js:
            json.dump(users, js, indent = 4)
        return "1"
    else:
        pass
