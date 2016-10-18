import re
import praw
user_agent = ("FRESH rookie 1.0")
r= praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit("hiphopheads")
def query():
	fresh_tracks = []
	for submission in subreddit.get_hot(limit=20):
		if re.search('\[FRESH( .*)?\]', submission.title):
			fresh_tracks=fresh_tracks + [(submission.title, submission.permalink)]
	return fresh_tracks
l=query()
for song in l:
		print song[0]
