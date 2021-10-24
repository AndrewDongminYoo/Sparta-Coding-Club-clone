# -*- coding: utf-8 -*-
from flask import before_render_template, request, jsonify, make_response, Blueprint, json, abort, url_for, \
    render_template
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
        user_id = request.cookies.get("username")
        course_name = json.loads(request.data.decode('utf8'))['courseName']
        user = users.find_one({"uuid": user_id})
        courses_list = user['courses']
        if course_name in courses_list:
            return {"message": "courses already exists"}
        courses_list.append(course_name)
        print(courses_list)
        users.update_one({"uuid": user_id}, {"$set": user}, upsert=True)
        response = make_response(jsonify(courses_list))
        response.set_cookie("course", course_name)
        return response


@bp.route('/courses', methods=['GET', 'POST'])
def show_courses():
    if request.method == 'GET':
        user_id = request.cookies.get("username")
        course_name = request.cookies.get('course')
        user = users.find_one({"uuid": user_id})
        courses_list = user['courses']
        lecture = list(lectures.find(
            {"course_title": course_name}, {"_id": False, "link": False}))
        if course_name in courses_list:
            done = user["done"]
            seen = user["seen"]
            return jsonify({"done": done, "seen": seen, "courses": lecture})
        else:
            print("Cannot Open Course--")
            return abort(401)
    elif request.method == "POST":
        # 강의 페이지로 넘어가기 위한 유효성 검사
        return


@bp.route('/lecture', methods=['GET', 'POST'])
def show_lecture():
    if request.method == 'GET':
        # 강의의 회차 수 정보를 받아 디비에 있는 해당 주차 수업 영상 주소를 리턴
        pass
    elif request.method == "POST":
        # 강의를 다 보았을 때나 다른 강의로 넘어가려 할 때 가능한지 체크 후 리턴
        pass

