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
    #####################
    #finds the lowest score for the student
    ####################
    
    ##find all documents related to the person##
    print "find reporting for duty"
    query = {'name':'Tressa Schwing'}
    #projection = {'score':1} #limits data that is sent to the query ie. scores
    
    try:
        #cursor = records.find(query,projection)
        cursor = records.find(query)
    except Exception as e:
        print "Unexpected error:", type(e), e
    ##compare and find the _id of the document with the lowest score##
    lowest_score = 100 
    
    for docu in cursor:
        
        intermediate_score = docu['scores'][0]['score'] #needs work. its not always the first element is type exam!!
        
        #print "Intermediate_score: {}".format(intermediate_score)
        if lowest_score < intermediate_score:           #potential to crash since first instance (lowest_score =100) does not have record id
            print "if loop. Record id: {}".format(record_id)
            
        else:
            lowest_score = intermediate_score
            record_id = docu['_id']    #records the record_id for the lowest score
            print "else loop. Record id: {}".format(record_id)
                  
    print "Lowest Score: {}\nRecord Id:{}".format(lowest_score,record_id)
    ##Update_one to remove only the exam score of the identified _id
    result = records.update_one({'_id':record_id},{'$unset':{'scores.0.score': ''}})
    
    pprint.pprint(records.find_one({'_id':record_id})) #prints the score for review. 
    
    
        
        
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

#pprint.pprint(findOne())
pprint.pprint(find())
#pprint.pprint(student_names())    
    
