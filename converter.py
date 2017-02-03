import json
import os
from mappings import *

def format_raw_data():
	outputData = {}

	with open('data/Quran.json') as json_data:
		d = json.load(json_data)
		d = d['quran']['en.arberry']

		quran = [x for x in d.values()]
		quran = sorted(quran, key = lambda x: (x['surah'], x['ayah']))
		outputData['quran'] = quran

	with open('data/Bible.json') as json_data:
		d = json.load(json_data)

		bible = []
		for bookName, book in d.items():
			for chapterNum, chapter in book.items():
				for passageNum, passage in chapter.items():
					bible.append({
						"text"		: passage,
						"verse"		: passageNum,
						"chapter"	: chapterNum,
						"book"		: getNumFromBook(bookName)
					})

		bible = sorted(bible, key = lambda x: (x['book'], x['chapter'], x['verse']))
		outputData['bible'] = bible

	with open('data/formatted_data.json', 'w') as outfile:
		json.dump(outputData, outfile, indent = 4)