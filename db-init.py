# -*- coding: utf-8 -*-
from pymongo import MongoClient
from apps.models import Lecture
from uuid import uuid4
import os
import csv

client = MongoClient('localhost', port=27017)
db = client.get_database('Lecture')
os.popen('mongod')


def get_DB():
    with open("C:/Users/ydm27/Downloads/lectures.csv", mode="r", encoding="UTF-8", newline="") as input_file:
        reader = csv.reader(input_file)
        reader.__next__()
        for line in reader:
            doc = Lecture(
                title=line[1],
                course_title=line[0],
                order=line[2],
                week=line[3],
                week_order=line[4],
                link=line[5],
                playtime=line[6],
                seen=False,
                lecture_id=uuid4()
            )
            db.lectures.insert_one(doc.to_mongo())


if __name__ == '__main__':
    get_DB()
