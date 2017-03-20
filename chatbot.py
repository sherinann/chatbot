from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
def greetings_check(sentence):
	for word in sentence:
		if word.lower() in GREETING_KEYWORDS:
			return random.choice(GREETING_RESPONSES)

train = [
     ('I love this sandwich.', 'pos'),
     ('this is an amazing place!', 'pos'),
     ('I feel very good about these beers.', 'pos'),
     ('this is my best work.', 'pos'),
     ("what an awesome view", 'pos'),
     ('I do not like this restaurant', 'neg'),
     ('I am tired of this stuff.', 'neg'),
     ("I can't deal with this", 'neg'),
     ('he is my sworn enemy!', 'neg'),
     ('my boss is horrible.', 'neg'),
     ("i hate you.",'neg'),
     ("i love mangoes.",'pos')
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



#if__name__== "__main__":
cl = NaiveBayesClassifier(train)

sentence="hey how are you"
b=TextBlob(sentence)
# text=b.lower()
#text=b.correct()

#print(cl.classify(text))
#prob_dist = cl.prob_classify(text)
#print(round(prob_dist.prob("pos"), 2
for sentence.words in sentence:
	print(sentence.words)
	if sentence.words in GREETING_KEYWORDS:
		print("yes")
t=greetings_check(sentence)
print(t)