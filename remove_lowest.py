# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 13:34:21 2018

@author: WTeo2
"""

from pymongo import MongoClient
import sys
import pprint


client = MongoClient()
db = client.school
records = db.students

### for printing all the records in the collection 
'''
for record in records.find():
    print records.find_one()

    
'''
def findOne():
    print "findOne, reporting for duty"
    query = {'name':'Gisela Levin'} #
    
    try: 
        doc = records.find_one(query)
        print doc
        #studentname = doc["name"]
        #print studentname
        
    except Exception as e:
        print "Unexpected error:", type(e), e
    
def find():
    print "find reporting for duty"
    
    query = {'name':'Gisela Levin'}
    projection = {'scores':1} #limits data that is sent to the query ie. scores
    
    try:
        cursor = records.find(query,projection)
                
    except Exception as e:
        print "Unexpected error:", type(e), e
        
    for docu in cursor:
        pprint.pprint(docu)

def student_names():
    ###########
    #Pulls the unique student names and returns it in an array
    ###########
    
    print "student_names reporting"
    query = {}
    projection = {'name': 1}
    
    try:
        cursor = records.find(query,projection)
    
    except Exception as e:
        print "Unexpected error:", type(e), e
    name_array = []
    for names in cursor.distinct("name"): #gets the unique occurences of each name distinct() is a method in pymongo.collections
        #print type(names)
        names = names.encode("utf-8") #converts the unicode to python str
        name_array.append(names)      
    
    
    return name_array

#def pull_score(name_array):
    #pulls the score with type exam
    

#pprint.pprint(findOne())
pprint.pprint(find())
#pprint.pprint(student_names())    
    
