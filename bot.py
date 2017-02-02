import tweepy
import os
from image_generator import generateImage

API_KEY             = os.environ['API_KEY']
API_SECRET          = os.environ['API_SECRET']
ACCESS_TOKEN        = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

imagePath, (quranFooter, bibleFooter) = generateImage()
statusText = '{0}\n{1}'.format(quranFooter, bibleFooter)

api.update_with_media(imagePath, statusText)
os.remove(imagePath)