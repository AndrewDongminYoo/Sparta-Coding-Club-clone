from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os

application = Flask(__name__, static_folder='static', template_folder='templates')
client = MongoClient('localhost', port=27017)
db = client.get_database('Lecture')
if application.env == 'development':
    os.popen('mongod')
    application.debug = True


@application.route('/')
def hello_world():  # put application's code here
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


if __name__ == '__main__':
    application.run()
