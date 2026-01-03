from auth import *
from keywords import *

def main():
    # the main programm opens
    name = request()

    print('''\n▗▖ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖     ▗▖  ▗▖▗▄▄▖  ▗▄▖  ▗▄▄▖
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌         █ ▐▌ ▐▌    ▐▛▚▞▜▌▐▌ ▐▌▐▌ ▐▌▐▌
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘      █ ▐▌ ▐▌    ▐▌  ▐▌▐▛▀▘ ▐▌ ▐▌ ▝▀▚▖
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖      █ ▝▚▄▞▘    ▐▌  ▐▌▐▌   ▝▚▄▞▘▗▄▄▞▘
                                                                          ''')

    print("print help to list comands")
    print()

    while True:
        exitOrReboot = keywords(name)

        if exitOrReboot == 'e':
            print("byeeeee!")
            break

        if exitOrReboot == 'r':
            print("Rebooting...\n")
            del name
            startingProg()

if __name__ == "__main__":
    main()
