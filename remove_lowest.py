# -*- coding: utf-8 -*-
"""
Created on Thu Apr 05 13:34:21 2018

@author: WTeo2

Pending iteration for all names!
"""

from pymongo import MongoClient
import sys
import pprint
import time


client = MongoClient()
db = client.school
records = db.students
  
def find(student):
    #####################
    #finds the lowest score for the student
    ####################
    if student == '':#removes the blank document at the end of the student array
        return
    #######find all documents related to the person######
    else:
        print "find reporting for duty\n\n"
        query = {'name':student}
                
        try:
            cursor = records.find(query)
        except Exception as e:
            print "Unexpected error:", type(e), e
           
        ######compare and find the _id of the document with the lowest score#######
        lowest_score = 100 
        print "###############\nChecking Student: {}\n\n###############".format(student)
        for docu in cursor:
            print "findscore for loop running\n"
            ######compare and find the _id of the lowest homework score in the array###
            if docu['scores'][2]['score'] < docu['scores'][3]['score'] :
                inter_score = docu['scores'][2]['score'] 
                array_pos = 2
            else:
                inter_score = docu['scores'][3]['score'] 
                array_pos = 3
                
            #intermediate_score = docu['scores'][0]['score'] #needs work. its not always the first element is type exam!! maybe its ok.
            #record_id = docu
            print "Record: {}, Lowest Homework: {}\n".format(docu['_id'],inter_score)
        
            if lowest_score < inter_score:           #potential to crash since first instance (lowest_score =100) does not have record id
                print "if loop"
                
            else:
                lowest_score = inter_score
                record_id = docu['_id']    #records the record_id for the lowest score
                      
        print ">>>>>>>>\nLowest Score: {}\nRecord Id:{}\n>>>>>>>>\n".format(lowest_score,docu['_id'])
        ##Update_one to remove only the exam score of the identified _id
        ## have to do if == 2 since $unset does not accept variable in scores.var.score
        if array_pos == 2:
            result = records.update_one({'_id':record_id},{'$unset':{'scores.2.score': ''}})
        else:
            result = records.update_one({'_id':record_id},{'$unset':{'scores.3.score': ''}})
        
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
        
        names = names.encode("utf-8") #converts the unicode to python str
        name_array.append(names)      
    
    
    return name_array

#pprint.pprint(findOne())
#pprint.pprint(find())
#pprint.pprint(student_names())    

#print "Student list: {}".format(student_list)

student_list = (student_names())

print "Number of students: {}\n".format(len(student_list))
time.sleep(5) #just for my sanity
for idx, student in enumerate(student_list):
    print "{} student for loop running".format(idx)  
    find(student)
    
print ("EOL")

