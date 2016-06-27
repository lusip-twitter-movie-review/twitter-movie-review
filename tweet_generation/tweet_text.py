import json
import re
import unicodedata
import os

input_file = os.path.join(
	os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
	'data',
	'movie_data.json'
)

input_file = open(input_file)
tweets = []
for line in input_file:
	try:
		temp_json = json.loads(line)
		if temp_json['text']:
			t = temp_json['text']
			t = re.sub('https?:/*[\w\./]*', "", t)
			t = re.sub('\\bRT\\b|#|@'," ", t)
			t = unicodedata.normalize('NFKD', t).encode('ascii','ignore') 
			tweets.append(t)
	except ValueError as ex:
		pass

output_file = os.path.join(
	os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
	'data',
	'extacted_tweets.json')
output_file = open(output_file, "w")
input_file.close()
output_file.write(json.dumps(tweets, indent=4))
output_file.close()
