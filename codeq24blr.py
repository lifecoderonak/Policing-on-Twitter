import tweepy
import datetime
import matplotlib.pyplot as plt

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
countPhotos = 253
countVideos = 7
username = "@BlrCityPolice"
tmpTweets = api.user_timeline(username)

for tweet in tmpTweets:
	if(tweet.created_at < endDate and tweet.created_at > startDate):
		#print tweet.id
		# print tweet.text
		# print tweet.created_at
		tweets.append(tweet)
		#print tweet.text

while(tmpTweets[-1].created_at > startDate):
	tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
	for tweet in tmpTweets:
		if(tweet.created_at < endDate and tweet.created_at > startDate):
			tweets.append(tweet)
			# print tweet.created_at
			# print tweet.text
#print countTweets
countTweets = len(tweets)
print 'Number of Tweets :-'
print countTweets
print 'Number of Photos :-'
print countPhotos
print 'Number of Videos :-'
print countVideos
print 'Number of Text Tweets'
countText = countTweets - (countVideos + countPhotos)
print countText
labels = ['Photos', 'Videos', 'Text']
sizes = [countPhotos, countVideos, countTweets-(countPhotos + countVideos)]
plt.pie(sizes, labels = labels, autopct='%1.1f%%')
plt.title('Pie Chart of Bengaluru Police Photos, Videos & Text')
plt.show()
				


				
