import tweepy
import pylab
import matplotlib.pyplot as plt
import datetime
import pandas
import numpy as np
import pylab
import time
from time import sleep

consumer_key = 'T0835oldFAK9mShRV0RUwJCOI'
consumer_secret = 'HcKyQpDefYRQnxqcnRNFrbtnruJuT7qpGcNhdQKNs2w80L3jSV'
access_token = '736121499359186944-SD9qK238pS1wQgi31SsGEOnDCktFVMC' 
access_token_secret = 'pdrL8CaCoLasFyrbLEro53HkA4iLMHFcHW4iTp76gVnJL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

startDate = datetime.datetime(2017, 8, 1, 0, 0, 0)
endDate = datetime.datetime(2017, 9, 8, 0, 0, 0)

# startDate = datetime.datetime(2017, 8, 1, 5, 30, 0)
# endDate = datetime.datetime(2017, 9, 8, 5, 30, 0)

username = "@BlrCityPolice"
tmpTweets = api.user_timeline(username)
reTweets = {}
for tweet in tmpTweets:
	words = []
	if(tweet.created_at < endDate and tweet.created_at > startDate):
		text = tweet.text
		#print tweet.created_at
		#print text
		words = text.split(" ")
		if(words[0] == "RT"):
			#print words
			reTweeter = words[1]
			#print reTweeter
			if(reTweeter not in reTweets):
				reTweets[reTweeter] = 1
			else:
				count = reTweets[reTweeter]
				reTweets[reTweeter] = count+1	

while(tmpTweets[-1].created_at > startDate):
	tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
	words = []
	for tweet in tmpTweets:
		if(tweet.created_at < endDate and tweet.created_at > startDate):
			text = tweet.text
			#print tweet.created_at
			#print text
			words = text.split(" ")
			if(words[0] == "RT"):
				#print words
				reTweeter = words[1]
				#print reTweeter
				if(reTweeter not in reTweets):
					reTweets[reTweeter] = 1
				else:
					count = reTweets[reTweeter]
					reTweets[reTweeter] = count+1
print 'Handles are :-'
cnt = 0	
labels = []
values = []				
for key, value in sorted(reTweets.iteritems(), key = lambda (k,v): (v,k), reverse = True):
	print key, value
	labels.append(key)
	values.append(value)
	cnt += 1
	if(cnt == 10):
		break
plt.pie(values, labels = labels, autopct='%1.1f%%')
plt.title('Pie Chart of Top ReTweeted IDS Bengaluru Police')
plt.show()		


