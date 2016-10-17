import os
import time
import twitter
import scrapper
#Get account information from console.
token=os.environ['TWITTER_ACCESS_TOKEN_KEY']
token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
key=os.environ['TWITTER_CONSUMER_KEY']
key_secret=os.environ['TWITTER_CONSUMER_SECRET']
#log in to twitter
auth=twitter.OAuth(token, token_secret, key, key_secret)
client = twitter.Twitter(auth=auth)
while True:
	fresh_tracks = scrapper.query()
	for track in fresh_tracks:
		client.statuses.update(status=track)
		print "querying!!!"
	time.sleep(3600)
