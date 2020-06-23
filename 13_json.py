# API's
#API means application programming interface

#JSON is (JavaScript Object Notation) is a lightweight data-interchange format.
#It is easy for humans to read and write. It is easy for machines to parse and generate.

# Javascript object is like a python dictionary

import requests
#we chose a web page with trivia 
r = requests.get("https://opentdb.com/api.php?amount=1&category=15&difficulty=easy&type=multiple")

#the above is to get the data stored on that webpage. It had only one trivia question

import json #use the json module



question = json.loads(r.text) # this assigns the text of the question to a variable

# the type is a dictionary

import pprint #this loads a module to convert to python readable

pprint.pprint(question) #this converts it to a more readable format

question['results'][0]['category'] # this pulls the first key of the question

#now we can practice taking it from a dictionary to a json style question

person = {'name':'Paul','age':30}# this is a dictionary

person_json = json.dumps(person) #this converts it to json

person_json #to show how it looks after converted back
