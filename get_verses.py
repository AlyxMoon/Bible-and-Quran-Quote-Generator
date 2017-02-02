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

def getRandomVerse():
    if os.path.isfile('data/formatted_data.json'):
        if os.path.isfile('data/unused_quotes.json'):
            data, bible, quran = {}, {}, {}
            with open('data/unused_quotes.json') as json_data:
                data = json.load(json_data)

                if len(data['bible']) == 0 or len(data['quran']) == 0:
                    with open('data/formatted_data.json') as whole_json_data:
                        wholeData = json.load(whole_json_data)
                        if len(data['bible']) == 0: data['bible'] = wholeData['bible']
                        if len(data['quran']) == 0: data['quran'] = wholeData['quran']

                bible = data['bible'].pop(randint(0, len(data['bible']) - 1))
                quran = data['quran'].pop(randint(0, len(data['quran']) - 1))

            os.remove('data/unused_quotes.json')
            with open('data/unused_quotes.json', 'w') as outfile:
                json.dump(data, outfile, indent = 4)

            return (bible, quran)

        else:
            with open('data/formatted_data.json') as json_data:
                d = json.load(json_data)
                newData = {
                    'bible': d['bible'],
                    'quran': d['quran']
                }
                with open('data/unused_quotes.json', 'w') as outfile:
                	json.dump(newData, outfile, indent = 4)
                return getRandomVerse()
    else:
        import converter
        return getRandomVerse()