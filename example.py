import json
import os
from random import randint
from mappings import *

def printRandomVerse():
    if os.path.isfile('data/formatted_data.json'):
        with open('data/formatted_data.json') as json_data:
            d = json.load(json_data)

            bible = d['bible'][randint(0, len(d['bible']))]
            print('Bible -- {0} {1}:{2}'.format(getBookFromNum(bible['book']), bible['chapter'], bible['verse']))
            print(bible['text'])

            quran = d['quran'][randint(0, len(d['quran']))]
            print('Quran -- {0} | Verse {1}'.format(getSurahFromNum(quran['surah']), quran['ayah']))
            print(quran['verse'])

    else:
        print('Formatting data...')
        import converter
        printRandomVerse()

printRandomVerse()