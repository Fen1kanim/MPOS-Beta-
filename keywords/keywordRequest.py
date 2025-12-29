from subprocess import call
import json
import datetime
import os
from keywords.calc import calc
from keywords.delete import delete
from keywords.help import help
from keywords.uranium import uranium

def keywords():
    #import databases
    with open('keywords.json', 'r') as js:
        keywords = json.load(js)
    with open('./authentification/lastUser.json', 'r') as js:
        lastUser = json.load(js)
    with open('./authentification/users.json', 'r') as js:
        users = json.load(js)

    #main loop
    while True:
        stdin = input("--> ") # as user for any commands

        call(["python", "./keywords/games/menu.py"]) \
        if stdin in keywords["game"] else None # game

        uranium() if stdin in keywords['uranium'] else None # uranium

        # help
        help() if stdin in keywords['help'] else None

        print('you are as', lastUser["name"], 'authorized') \
        if stdin in keywords['whoami'] else None # whoami

        print('Hi! How r u?')  if stdin in keywords['hi'] else None # hi

        print('It is', datetime.datetime.now().strftime("%H:%M")) \
        if stdin in keywords['time'] else None # time

        delete() if stdin in keywords['delete'] else None # delete account

        print('Today is', datetime.datetime.now().strftime("%d %B of %y")) \
        if stdin in keywords['date'] else None # date

        os.system('clear') if stdin in keywords['clear'] else None # clear

        open() if stdin in keywords['open'] else None
        # open

        calc() if stdin in keywords['calc'] else None
        # calc

        # unknown command
        if stdin not in keywords['game'] \
        and stdin not in keywords['uranium'] \
        and stdin not in keywords['help'] \
        and stdin not in keywords['whoami'] \
        and stdin not in keywords['hi'] \
        and stdin not in keywords['time'] \
        and stdin not in keywords['delete'] \
        and stdin not in keywords['date'] \
        and stdin not in keywords['clear'] \
        and stdin not in keywords['open'] \
        and stdin not in keywords['calc'] \
        and stdin != 'exit':
            print('sorry, unknown command\ntry again')

        if stdin == 'exit': # exit to terminal
            print("byeee")
            break
