# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, current_user
from pymongo import MongoClient
import os
import json

application = Flask(__name__, static_folder='static', template_folder='templates')
if application.env == 'development':
    os.popen('mongod')
    application.debug = True
client = MongoClient('localhost', port=27017)
db = client.get_database('Lecture')
lectures = db.get_collection('lectures')
config_file = open("./config.json", mode="r")
config_json = json.load(config_file)
SECRET_KEY = config_json["SECRET_KEY"]
login_manager = LoginManager()
login_manager.init_app(application)


@application.route('/')
def hello_world():
    return 'Hello World!'


@application.route('/enrollment')
def enrollment():
    return render_template('EnrollPage.html', course_name="웹개발종합반")


@application.route('/lecture')
def show_video():
    return render_template('LecturePage.html')


@application.route('/roadmap')
def show_roadmap():
    return render_template('RoadmapPage.html')


@application.route('/api/courses', methods=['GET', 'POST'])
def show_courses():
    if request.method == 'GET':
        pass
    elif request.method == "POST":
        pass


@application.route('/api/enrollment', methods=['GET', 'POST'])
def post_enrollment():
    if request.method == 'GET':
        pass
    elif request.method == "POST":
        token = request.cookies.get('spartan_name')


@application.route('/api/lecture', methods=['GET', 'POST'])
def show_lecture():
    if request.method == 'GET':
        pass
    elif request.method == "POST":
        pass


@login_manager.user_loader
def load_user(uuid):
    return get(uuid)


if __name__ == '__main__':
    application.run()
