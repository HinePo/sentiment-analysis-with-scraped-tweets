import time
import twitter
from textblob import TextBlob

start = time.time()

# First we must create a twitter developer account and provide the strings below
consumerKey = 'put yours here'
consumerSecret = 'put yours here'
OauthToken = 'put yours here'
OauthSecret = 'put yours here'

# Authenticate and setup the Twitter API object
authInfo = twitter.oauth.OAuth(OauthToken, OauthSecret, consumerKey, consumerSecret)
twitterAPI = twitter.Twitter(auth=authInfo)

# search and scrape twitter topic
# docs: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
topic = "#starwars"
searchResults = twitterAPI.search.tweets(q=topic,count=100)

List_of_tweets = []
List_score = []

medium_score = 0
k=1
for tweet in searchResults["statuses"]:

	if TextBlob(tweet["text"]).sentiment.polarity != 0:
		print("\n",k, tweet["text"])

		# sentiment analysis
		blob = TextBlob(tweet["text"])
		score = blob.sentiment.polarity
		print(score)

		List_of_tweets.append(tweet["text"])
		List_score.append(score)

		medium_score = medium_score + score

		k = k + 1

# print(List_of_tweets)
# print(List_score)
print('\n\nSearched topic: ', topic)
print('Score range: -1 <= score <= 1')
print('Medium score: ', medium_score/(k-1))
print('Analysed tweets: ', k-1)

end = time.time()
elapsed = (end-start)
print('Task performed in ', elapsed, 'seconds')