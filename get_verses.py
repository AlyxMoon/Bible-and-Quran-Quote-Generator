import json
import os
from random import randint
from mappings import *
from converter import format_raw_data

def getRandomVerse():
    if os.path.isfile('data/formatted_data.json'):
        with open('data/formatted_data.json') as json_data:
            data = json.load(json_data)

            bible = data['bible'][randint(0, len(data['bible']) - 1)]
            quran = data['quran'][randint(0, len(data['quran']) - 1)]

            bible['citation'] = 'Bible -- {0} {1}:{2}'.format(getBookFromNum(bible['book']), bible['chapter'], bible['verse'])
            quran['citation'] = 'Quran -- {0} | Verse {1}'.format(getSurahFromNum(quran['surah']), quran['ayah'])

            return (bible, quran)
    else:
        format_raw_data()
        return getRandomVerse()