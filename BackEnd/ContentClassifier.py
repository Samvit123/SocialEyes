# -*- coding: utf-8 -*-
import time
import argparse
import io
import json
import os

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six
import timeout_decorator
import signal

poffensive = 0
loffensive = 0

poffensive_list = []
loffensive_list = []


client = language.LanguageServiceClient()


f=open("/home/samvit/Desktop/lastoutput.txt","w+")
f.close()

fo=open("/home/samvit/Desktop/lastoutput.txt","w")
fo.close()


def classify(text, verbose=True):
    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)

    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    return result

with open("/home/samvit/Desktop/outputone.txt","r") as o:
    r=o.readlines()

i=0
total = 0
neutral=0
while i<len(r):
    text= str(r[i]).rstrip('\n')

    s = text.split(" ")
    text2=""

    for v in s:
        if "@" in v:
            s.remove(v)

    for v in s:
        if "@" in v:
            s.remove(v)

    for v in s:
        text2=text2+" "+v


    text=text2[1:]

    text1 = text
    while len(text.split(" "))<=20:
        text = text+" "+text1

    try:
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        analysis = classify(text)
        if analysis:
            for key in analysis:
                with open("/home/samvit/Desktop/lastoutput.txt","a+") as w:
                    w.write("category: "+key+" ")
                    w.write("confidence: "+str(analysis[key]))
                    w.write("\n")

                elif (("people & society" in key.lower() or "sensitive subjects" in key.lower()) and (float(analysis[key])<0.5 and sentiment.score>-0.25)):
                    poffensive+=1
                    poffensive_list.append(text1)
                elif (("people & society" in key.lower() or "sensitive subjects" in key.lower()) and ((float(analysis[key])>=0.5) and sentiment.score<=-0.25)) or "adult" in key.lower():
                    loffensive+=1
                    loffensive_list.append(text1)
                else:
                    pass
                    neutral+=1
                print (i)
                total+=1
                break
        else:
            with open("/home/samvit/Desktop/lastoutput.txt","a+") as w:
                w.write("\n")

    except:
    	with open("/home/samvit/Desktop/lastoutput.txt","a+") as w:
            w.write("\n")

    i+=1

with open("/home/samvit/Desktop/final.txt","a+") as w:
    w.write("\n\nContent Distribution: ")
    w.write("\nPercent potentially offensive: "+str(float(poffensive/total)*100))
    w.write("\nPercent likely offensive: "+str(float(loffensive/total)*100))
    w.write("\nPercent neutral: "+str(float(neutral/total)*100))

    w.write(("\n\nPotentially offensive:"))
    for v in poffensive_list:
        w.write("\n"+v)

    w.write(("\n\nLikely offensive:"))
    for v in loffensive_list:
        w.write("\n"+v)

print ("------------")
print (total)
print(poffensive)
print (loffensive)
print ("------------")
print ("Profanity list: ")
print (profanity_list)
print ("Potentially offensive list: ")
print (poffensive_list)
print ("Likely offensive list: ")
print (loffensive_list)
