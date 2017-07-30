from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob import Word
import random

def greetings_check(tb):
	for word in tb.words:
		if word.lower() in GREETING_KEYWORDS:
			return random.choice(GREETING_RESPONSES)

def reply_engine(sentence,train):
    cl = NaiveBayesClassifier(train)
    k = str(cl.classify((sentence)))
    if k == 'pos':
        return random.choice(POSITIVE_RESPONSE)
    elif k == 'neg':
        return random.choice(NEGATIVE_RESPONSE)


train = [
     ('I love this sandwich.', 'pos'), ('this is an amazing place!', 'pos'),
     ('I feel very good about these beers.', 'pos'),
     ('this is my best work.', 'pos'),
     ("what an awesome view", 'pos'),
     ('I do not like this restaurant', 'neg'),
     ('I am tired of this stuff.', 'neg'),
     ("I can't deal with this", 'neg'),
     ('he is my sworn enemy!', 'neg'),
     ('my boss is horrible.', 'neg'),
     ("i hate you.",'neg'),
     ("i love mangoes.",'pos'),
     ("i am sad.", 'neg')
]

test = [
     ('the beer was good.', 'pos'),
     ('I do not enjoy my job', 'neg'),
     ("I ain't feeling dandy today.", 'neg'),
     ("I feel amazing!", 'pos'),
     ('Gary is a friend of mine.', 'pos'),
     ("I can't believe I'm doing this.", 'neg')

]

GREETING_KEYWORDS = ("hello","hey", "hi", "greetings", "sup", "what's up","namaste")

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

POSITIVE_RESPONSE = ["wow thats cool", "amazing", "you are awesome", "happy to hear that"]
NEGATIVE_RESPONSE = ["thats bad", "i am sorry", "this is embarassing", "its ok"]



print('Hi I\'m Jessy. Ask me something')
sentence = input()

while sentence.lower() != 'bye':
   tb = TextBlob(sentence)
   t = str(greetings_check(tb))
   if t == 'None':
       t = reply_engine(tb,train)
   print(t)
   sentence = input()
print('Bye,Have a nice day!')
