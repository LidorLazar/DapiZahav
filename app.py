import json
from DapiZahav import*

contact = []
FILE_JSON = 'contact.json'

def manu():
    book = DapiZahav()
    with open(FILE_JSON, 'r') as f:
        phonebook = json.load(f)
        print(phonebook)
    book.add_contact('lidor', '3432')


if __name__ == "__main__":
    print(manu())