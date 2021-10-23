# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response, Blueprint
from pymongo import MongoClient

me = MongoClient()
le = me.get_database("Lecture")
users = le.get_collection("users")
lectures = le.get_collection("lectures")
courses = le.get_collection("courses")

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/enrollment', methods=['GET', 'POST'])
def post_enrollment():
    if request.method == 'GET':
        title = request.args.get("title")
        course = courses.find_one({"title": title}, {"_id": False})
        return jsonify(course)
    elif request.method == "POST":
        print("POST")
        user_id = request.cookies.get("username")
        print(user_id)
        course_name = request.path.split("/")[-1]
        print(course_name)
        user = users.find_one({"_id": user_id})
        print(user)
        pass


@bp.route('/courses', methods=['GET', 'POST'])
def show_courses():
    if request.method == 'GET':
        pass
    elif request.method == "POST":
        # 강의 페이지로 넘어가기 위한 유효성 검사
        pass


@bp.route('/lecture', methods=['GET', 'POST'])
def show_lecture():
    if request.method == 'GET':
        # 강의의 회차 수 정보를 받아 디비에 있는 해당 주차 수업 영상 주소를 리턴
        pass
    elif request.method == "POST":
        # 강의를 다 보았을 때나 다른 강의로 넘어가려 할 때 가능한지 체크 후 리턴
        pass

