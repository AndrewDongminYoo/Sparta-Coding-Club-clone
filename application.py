from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

application = Flask(__name__, static_folder='static', template_folder='templates')
if application.env == 'development':
    os.popen('mongod')
    application.debug = True
client = MongoClient('localhost', port=27017)
db = client.get_database('Lecture')
classes = db.get_collection('lectures')


@application.route('/')
def hello_world():
    return 'Hello World!'


@application.route('/enrolment')
def enrolment():
    return render_template('EnrollPage.html')


@application.route('/lecture')
def show_video():
    return render_template('LecturePage.html')


@application.route('/roadmap')
def show_roadmap():
    return render_template('RoadmapPage.html')


@application.route('/api/class', methods=['GET'])
def show_class():

    classes.find({})


if __name__ == '__main__':
    application.run()
