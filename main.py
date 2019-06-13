import os
import tweepy
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
	
def main():
	setting()
	
	auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	redirect_url = auth.get_authorization_url()
	print('Please verify at: ' + redirect_url)
	
	pin = input('input PIN code:')
	auth.get_access_token(pin)

	

if __name__ == '__main__':
	main()