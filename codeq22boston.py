import tweepy
import pylab
import matplotlib.pyplot as plt
import datetime
from pylab import *
import random
import time

consumer_key = 'T0835oldFAK9mShRV0RUwJCOI'
consumer_secret = 'HcKyQpDefYRQnxqcnRNFrbtnruJuT7qpGcNhdQKNs2w80L3jSV'
access_token = '736121499359186944-SD9qK238pS1wQgi31SsGEOnDCktFVMC' 
access_token_secret = 'pdrL8CaCoLasFyrbLEro53HkA4iLMHFcHW4iTp76gVnJL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

startDate = datetime.datetime(2017, 8, 1, 0, 0, 0)
endDate = datetime.datetime(2017, 9, 8, 0, 0, 0)

tweets = []
likes = []
retweets = []
replies = []
username = "@BostonPolice"
tmpTweets = api.user_timeline(username)
for tweet in tmpTweets:
	try:
		if(tweet.created_at < endDate and tweet.created_at > startDate):
			print tweet.text
			print tweet.created_at
			print "Number of likes are : ", tweet.favorite_count
			print "Number of retweets are : ", tweet.retweet_count
			if(tweet.in_reply_to_status_id != None):
				print "Number of replies are : ", tweet.in_reply_to_status_id
				replies.append(tweet.in_reply_to_status_id)	
			else:
				replies.append(0)	
			likes.append(tweet.favorite_count)	
			retweets.append(tweet.retweet_count)
			tweets.append(tweet.id)
	except tweepy.TweepError:
		break
while(tmpTweets[-1].created_at > startDate):
	try:
		tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
		for tweet in tmpTweets:
			if(tweet.created_at < endDate and tweet.created_at > startDate):
				print tweet.text
				print tweet.created_at
				print "Number of likes are : ", tweet.favorite_count
				print "Number of retweets are : ", tweet.retweet_count
				if(tweet.in_reply_to_status_id != None):
					print "Number of replies are : ", tweet.in_reply_to_status_id
					replies.append(tweet.in_reply_to_status_id)	
				else:
					replies.append(0)	
				likes.append(tweet.favorite_count)
				retweets.append(tweet.retweet_count)		
				tweets.append(tweet.id)
	except tweepy.TweepError:
		break
aray = []
for i in replies:
	if(i != 0):
		aray.append(25)
	else:
		aray.append(0)	
print len(tweets)
print len(replies)
print len(likes)
print len(retweets)
#print replies
arr = []
count = 1
for i in range(0, len(tweets)):
	arr.append(count)
	count = count + 1
print '\n\n'
print "Green :- Likes"
print "Red :- Retweets"
print "Blue :- Replies"	
x = range(len(tweets))
pylab.figure(1)
pylab.xticks(x, arr)
pylab.xlabel("Tweet IDS")	
pylab.ylabel("Likes")
#pylab.legend(loc = 4)
pylab.title("Bengaluru Police User Responses (Likes, Retweets, Replies)")
pylab.plot(x, likes, "g", label = "Likes")
pylab.plot(x, retweets, "r", label = "Retweets")
pylab.plot(x, aray, "b", label = "Replies")
pylab.show()	

