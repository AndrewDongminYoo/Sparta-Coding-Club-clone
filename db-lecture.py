from pymongo import MongoClient
import os
import csv
from uuid import uuid4

client = MongoClient('localhost', port=27017)
db = client.get_database('Lecture')
os.popen('mongod')


def get_DB():
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


class Lecture:
    def __init__(self, course_title, title, order, week, week_order, link, playtime):
        self.done = False
        self.seen = False
        self.playtime = playtime
        self.enrolled_detail_id = uuid4()
        self.enrolled_id = uuid4()
        self.lecture_id = uuid4()
        self.order = order
        self.title = title
        self.course_title = course_title
        self.week = week
        self.week_order = week_order
        self.__link = link

    def __str__(self):
        return self.title
