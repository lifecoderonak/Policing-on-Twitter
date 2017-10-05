import tweepy
import pylab
import matplotlib.pyplot as plt
import datetime
import pandas
import numpy as np
import pylab

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

tweets = []
username = "@bostonpolice"
tmpTweets = api.user_timeline(username)

for tweet in tmpTweets:
	if(tweet.created_at < endDate and tweet.created_at > startDate):
		#print tweet.text
		#print tweet.created_at
		tweets.append(tweet.created_at)
		#tweets.append(tweet.text)

while(tmpTweets[-1].created_at > startDate):
	tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
	for tweet in tmpTweets:
		if(tweet.created_at < endDate and tweet.created_at > startDate):
			#print tweet.id
			#print tweet.text
			#print tweet.created_at
			tweets.append(tweet.created_at)
			#tweets.append(tweet.text)

date = ""
frequency = {}
labels = []
values = []
intial = 1
for tweet in tweets:
	date += str(tweet.month)
	date += "-"
	date += str(tweet.day)
	if(date not in frequency):
		frequency[date] = intial
	else:
		count = frequency[date]
		frequency[date] = count+1	
	date = ""
labels = []
values = []
for x in frequency:
	labels.append(x)
	values.append(frequency[x])
print labels, values
pylab.figure(1)
x = range(len(labels))
pylab.xticks(x, labels)
pylab.xlabel("Dates")
pylab.ylabel("Frequency of Tweets at particular Date")
pylab.plot(x, values, "g")
pylab.title("Boston City Police Frequency")
pylab.show()