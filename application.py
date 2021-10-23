# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify, make_response, abort, redirect
from pymongo import MongoClient
from uuid import uuid4
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


@application.route('/')
def hello_world():
    # 일단은 빈 페이지. 나중에 로그인 구현할 예정
    return 'Hello World!'


@application.route('/enrollment')
def enrollment():
    # 보안을 신경 쓰면서 쿠키를 주고받을 수 있도록 make_response 사용
    response = make_response(render_template('EnrollPage.html'))
    if not request.cookies.get("username"):
        response.set_cookie("username", uuid4().__str__())
    return response


@application.route('/lecture')
def show_video():
    if not request.cookies.get("username"):
        return abort(401)

    return render_template('LecturePage.html')


@application.route('/roadmap')
def show_roadmap():
    if not request.cookies.get("username"):
        return abort(401)
    return render_template('RoadmapPage.html')


if __name__ == '__main__':
    application.run(debug=True)
