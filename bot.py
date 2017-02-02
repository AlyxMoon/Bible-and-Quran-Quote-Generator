import tweepy
import os
from image_generator import generateImage
from tokens import *

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

imagePath, (quranFooter, bibleFooter) = generateImage()
statusText = '{0}\n{1}'.format(quranFooter, bibleFooter)

api.update_with_media(imagePath, statusText)
os.remove(imagePath)