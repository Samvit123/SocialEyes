from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

with open("/home/samvit/Desktop/outputone.txt","r") as o:
	r = o.readlines()

i = 0
pos_sent = 0
neg_sent = 0
neut_sent = 0
just_sent = ""

pos_tweets = []
neg_tweets = []
neut_tweets = []

client = language.LanguageServiceClient()

ro=open("/home/samvit/Desktop/output.txt","w")
ro.close()

while i<len(r):
	text = str(r[i])
	document = types.Document(
		content=text,
		type=enums.Document.Type.PLAIN_TEXT)

	sentiment = client.analyze_sentiment(document=document).document_sentiment

	
	if sentiment.score<-0.33:
		neg_sent+=1
		just_sent = "negative"
		neg_tweets.append(text)
	elif sentiment.score >0.33:
		pos_sent+=1
		just_sent = "positive"
		pos_tweets.append(text)
	else:
		neut_sent+=1
		just_sent = "neutral"
		neut_tweets.append(text)
	
	'''print('Text: {}'.format(text))
	print just_sent
	print "\n"'''
	
	i+=1

	
percent_neg = round((float(neg_sent)/i)*100)
percent_pos = round((float(pos_sent)/i)*100)
percent_neut = round((float(neut_sent)/i)*100)

with open("/home/samvit/Desktop/output.txt","a+") as w:
	w.write((str(percent_neg))+"\n")
	w.write((str(percent_pos)+"\n"))
	w.write((str(percent_neut)+"\n"))
