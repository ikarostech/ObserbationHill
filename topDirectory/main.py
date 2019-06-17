import os
import tweepy
import json
import statistics
from scipy import stats
from os.path import join, dirname
from dotenv import Dotenv
 
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

def setting():
	global CONSUMER_KEY
	global CONSUMER_SECRET
	dotenv = Dotenv(join(dirname(__file__),'.env'))
	os.environ.update(dotenv)

	CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
	CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')

def verify(auth):
	redirect_url = auth.get_authorization_url()
	print('Please verify at: ' + redirect_url)
	
	pin = input('input PIN code:')
	auth.get_access_token(pin)

	
	api = tweepy.API(auth)
	return api

def suspicious_index(user_detail):
	return user_detail.followers_count ** 2 / max((user_detail.statuses_count * user_detail.friends_count),1)

def analyze(api,screen_name):
	user_detail = api.get_user(screen_name=screen_name)
	followers_detail = api.followers(screen_name=screen_name)
			
	user_suspicious_index = suspicious_index(user_detail)
	followers_suspicious_index = stats.hmean([suspicious_index(s) for s in followers_detail])


	
	print("user suspicious_index: " + str(user_suspicious_index) )
	print("followers suspicious index: " + str(followers_suspicious_index) )
	print("delta index ratio: " + str(user_suspicious_index/followers_suspicious_index) )
def main():
	setting()
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	api = verify(auth)

	while True:
		user = input('input user\'s screen name ( @(.*?) ) or input \"quit\" : ')
		if user == 'quit':
			break
		analyze(api,user)
	

if __name__ == '__main__':
	main()