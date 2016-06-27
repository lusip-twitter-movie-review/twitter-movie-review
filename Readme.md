# Movie Review ratings from tweet analysis

The project will use lexicon/SVM methods to generate movie review ratings from twitter tweets

## Requirements
- python 2.7
- pip (`sudo apt-get install python-pip` on debian systems) 
- tweepy (`pip install tweepy`)
- nltk (`pip install nltk`)
- nltk data (`python -m nltk.downloader all`)

## How to run
- paste cred.json file to `tweet_generation/` folder
- Run `tweet_generation/tweet_extraction.py`
- Run `tweet_generation/tweet_text.py`
- (Optional) Run `lexicon_generation/sentinet.py`
- Run `tweet_analysis/processing.py`

> Please run the above scripts in their respective folders only

## The Todo list

### Use better preprocessing (Arush is handling this)
#### Problems :-

- Negation handling not working properly.

*Soln. 1:* removing `stopwords` were removing negation words. Stopped removing `stopwords`.


- Nouns are being included in sentiment analysis.

> The Shallows is a good movie.

Here shallow which is a noun in this context is included in rating with negative score.

*Soln 1:* remove all parts of speech except `verbs, adverbs or adjectives`  


- Sarcastic tweets generate a completely opposite ratings

- Getting only the tweets that are reviewing a movie instead of tweets that contain movie name

### Use SVM(support vector machines) (Romit is handling this)
#### Problems :-