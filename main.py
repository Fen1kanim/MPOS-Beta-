from subprocess import call
from authentification import request

# the main programm opens
request()

print('''\n▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖     ▗▖  ▗▖▗▄▄▖  ▗▄▖  ▗▄▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌         █ ▐▌ ▐▌    ▐▛▚▞▜▌▐▌ ▐▌▐▌ ▐▌▐▌
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘      █ ▐▌ ▐▌    ▐▌  ▐▌▐▛▀▘ ▐▌ ▐▌ ▝▀▚▖
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖      █ ▝▚▄▞▘    ▐▌  ▐▌▐▌   ▝▚▄▞▘▗▄▄▞▘
                                                                          ''')

print("print help to list comands")
print()

call(['python', './keywords/keywordRequest.py'])
