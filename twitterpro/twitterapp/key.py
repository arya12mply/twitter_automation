import tweepy
from django.conf import settings


auth = tweepy.OAuthHandler(settings.API_KEY,settings.API_KEY_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN,settings.ACCESS_TOKEN_SECRET)