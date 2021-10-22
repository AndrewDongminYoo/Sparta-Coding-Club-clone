from pymongo import MongoClient
import os
import csv

client = MongoClient('localhost', port=27017)
db = client.get_database('Lecture')
os.popen('mongod')


with open("C:/Users/ydm27/Downloads/lectures.csv", mode="r", encoding="UTF-8", newline="") as input_file:
    reader = csv.reader(input_file)
    first = reader.__next__()
    for line in reader:
        doc = dict()
        doc['course_title'] = line[0]
        doc['title'] = line[1]
        doc['order'] = line[2]
        doc['week'] = line[3]
        doc['week_order'] = line[4]
        doc['link'] = line[5]
        doc['playtime'] = line[6]
        db.lectures.insert_one(doc)