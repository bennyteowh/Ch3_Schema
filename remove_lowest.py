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
        print docu
    
#pprint.pprint(findOne())
pprint.pprint(find())
    
    
