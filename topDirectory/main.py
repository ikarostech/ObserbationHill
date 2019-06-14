import os
import tweepy
import json
import statistics
from scipy import stats
from os.path import join, dirname
from dotenv import load_dotenv
 
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

def setting():
	global CONSUMER_KEY
	global CONSUMER_SECRET
	dotenv_path = join(dirname(__file__),'.env')
	load_dotenv(dotenv_path)

	CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
	CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
def verify(auth):
	
	redirect_url = auth.get_authorization_url()
	print('Please verify at: ' + redirect_url)
	
	pin = input('input PIN code:')
	auth.get_access_token(pin)

def suspicious_index(user_detail):
	return user_detail.followers_count ** 2 / max((user_detail.statuses_count * user_detail.friends_count),1)

def analyze_user(api,user):
	user_detail = api.get_user(screen_name=user)
	followers_detail = api.followers(screen_name=user)
			
	user_suspicious_index = suspicious_index(user_detail)
	followers_suspicious_index = stats.hmean([suspicious_index(s) for s in followers_detail])


	
	print("user suspicious index: " + str(user_suspicious_index) )
	print("followers suspicious index: " + str(followers_suspicious_index) )
	print("delta index ratio: " + str(user_suspicious_index/followers_suspicious_index) )

def main():
	setting()
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	verify(auth)
	api = tweepy.API(auth)

	while True:
		print('input user\'s screen name ( @(.*?) ) or input \"quit\": ')
		user = input()
		if user == 'quit':
			break
		analyze_user(api,user)

if __name__ == '__main__':
	main()