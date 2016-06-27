import nltk
import neg
import json
import re
import unicodedata
import os
open_file = os.path.join(
	os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
	'data',
	'extacted_tweets.json'
)

tweets_file = open(open_file)
lemmatizer = nltk.stem.WordNetLemmatizer()

tweets = json.load(tweets_file)
pre_tweets = []
for tweet in tweets:
	tweet = unicodedata.normalize('NFKD', tweet).encode('ascii','ignore')
	tweet = " ".join([re.sub('(.)([A-Z][a-z]+)', r'\1 \2', i) for i in tweet.split()])
	tweet = tweet.lower()

	# word lemmatization
	# tweet = " ".join([lemmatizer.lemmatize(i) for i in tweet.split()])
	pre_tweets.append(tweet)

print ""
n = neg.Neg()
for i in range(len(pre_tweets)):
	tokenized = nltk.word_tokenize(pre_tweets[i])
	tagged = nltk.pos_tag(tokenized)
	# named_ent = nltk.ne_chunk(tagged)
	# print tagged
	# print type(tagged)
	# named_ent.draw()
	score = n.get_sentiments(tagged)

	if score>0:
		print "Positive Tweet:",tweets[i]
	elif score<0:
		print "Negative Tweet:",tweets[i]
	else:
		print "Neutral_Tweet:",tweets[i]
	print "score: " + str(score)
	print ""