import json

def ask4notes(name):
    with open('./keywords/notes/notes.json', 'r') as js:
        notes = json.load(js)

    if name in notes:
        print(f"your last note were: \"{notes[name]["note"]}\"")
    else:
        print('U hav no notes')

def takeANote(name):
    with open('./keywords/notes/notes.json', 'r') as js:
        notes = json.load(js)

    newNote = input('take a note: ')

    notes[name] = {"note": newNote}

    with open('./keywords/notes/notes.json', 'w') as js:
        json.dump(notes, js, indent=4)

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
