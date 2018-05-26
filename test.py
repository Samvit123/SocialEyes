# -*- coding: utf-8 -*-
import time
import argparse
import io
import json
import os

from google.cloud import language
import six
import timeout_decorator
import signal

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

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

text="@realDonaldTrump @washingtonpost @FoxNews This is what you fucking care about right now? Please step down you incompetent fuck."
text1 = text

while len(text.split(" "))<=20:
    text = text+" "+text1

s = text.split(" ")
text2=""

for v in s:
    if "@" in v:
        s.remove(v)

for v in s:
    if "@" in v:
        s.remove(v)

for v in s:
    text2=text2+v+" "

text=text2

print (text)

try:
    analysis = classify(text)
    print (analysis)
    if analysis:
        for key in analysis:
            print ("key is "+key)
    else:
        print ("Works fine")
except:
    print ("Still fine")
