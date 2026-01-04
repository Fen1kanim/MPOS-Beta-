import json
from keywords.notes.askNotes import ask4notes
from keywords.notes.takeANote import takeANote

def noteMenu(name):
    ask4notes(name)
    noteStdin = input("take a Note?(y\\n): ")
    if noteStdin == 'y':
        takeANote(name)
    elif noteStdin == 'n':
        pass
    else:
        print("try again")
        noteMenu(name)
