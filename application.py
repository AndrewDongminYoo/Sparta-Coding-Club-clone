# -*- coding: utf-8 -*-
import datetime
from flask import Flask, render_template, request, make_response, abort
from pymongo import MongoClient
from apps import apis
from flask_login import LoginManager
from apps.models import User
from uuid import uuid4
import os
import json
from flask_mongoengine import MongoEngine


application = Flask(__name__, static_folder='static', template_folder='templates')
application.register_blueprint(apis.bp)
application.config['MONGODB_SETTINGS'] = {
    "db": "Lecture",
    "port": 27017,
    "host": "localhost"
}
client = MongoEngine()
client.init_app(application)
if application.env == 'development':
    os.popen('mongod')
    application.debug = True
client = MongoClient('localhost', port=27017)
db = client.get_database('Lecture')
lectures = db.get_collection('lectures')
users = db.get_collection("users")
courses = db.get_collection("courses")
config_file = open("./config.json", mode="r")
config_json = json.load(config_file)
SECRET_KEY = config_json["SECRET_KEY"]
login_manager = LoginManager()
login_manager.init_app(application)


@application.route('/')
def hello_world():
    # 일단은 빈 페이지. 나중에 로그인 구현할 예정
    return 'Hello World!'


@application.route('/enrollment')
def enrollment():
    # 보안을 신경 쓰면서 쿠키를 주고받을 수 있도록 make_response 사용
    response = make_response(render_template('EnrollPage.html', course_name="웹개발 종합반"))
    if not request.cookies.get("username"):
        _id = uuid4().__str__()
        username = "test"
        password = "qwerty-is-week-pw"
        created_at = datetime.datetime.utcnow()
        seen = []
        doc = User(
            uuid=_id,
            username=username,
            password=password,
            created_at=created_at,
            seen=seen,
            courses=[]
        )
        users.save(doc.to_mongo())
        response.set_cookie("username", _id)
        return response
    try:
        uuid = request.cookies.get("username")
        user = users.find_one({"id": uuid})
        response.set_cookie("user", json.dumps(user))
    finally:
        return response


@application.route('/roadmap')
def show_roadmap():
    if not request.cookies.get("username"):
        return abort(401)
    return render_template('RoadmapPage.html')


@application.route('/lecture/<string:lecture_id>')
def show_video(lecture_id):
    if not request.cookies.get("username"):
        return abort(401)
    lecture = lectures.find_one({"lecture_id": lecture_id}, {"_id": False})
    return render_template('LecturePage.html', lecture=lecture)


@login_manager.user_loader
def load_user(user_id):
    return lectures.find_one({"username": user_id}, {"_id": False})


if __name__ == '__main__':
    application.run(debug=True)
