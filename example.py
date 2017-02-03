from get_verses import getRandomVerse

(bible, quran) = getRandomVerse()

print(quran['citation'])
print(quran['verse'])

print(bible['citation'])
print(bible['text'])