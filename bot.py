import tweepy
import os
from random import randint
from get_verses import getRandomVerse
from image_generator import generateImage

if randint(1, int(os.environ['RUN_CHANCE'])) == 1:
    API_KEY             = os.environ['API_KEY']
    API_SECRET          = os.environ['API_SECRET']
    ACCESS_TOKEN        = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    (bible, quran) = getRandomVerse()
    imagePath = generateImage(bible, quran)
    statusText = '{0}\n{1}'.format(quran['citation'], bible['citation'])

    api.update_with_media(imagePath, statusText)
    os.remove(imagePath)