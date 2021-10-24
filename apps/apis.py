# -*- coding: utf-8 -*-
from flask import request, jsonify, make_response, Blueprint, json, abort
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
            seen = user["seen"]
            return jsonify({"seen": seen, "course_title": course_name, "courses": lecture})
        else:
            print("Cannot Open Course--")
            return abort(401)
    elif request.method == "POST":
        user_id = request.cookies.get("username")
        course_name = request.cookies.get('course')
        body = json.loads(request.data.decode())
        order = body["order"]
        user = users.find_one({"uuid": user_id})
        courses_list = user['courses']
        if course_name not in courses_list:
            print("you didn't pay for that...")
            return {"message": "올바르지 않은 접근입니다.", "status": 401}
        if order != 1:
            if order-1 not in user["seen"]:
                return {"message": "앞에 강의를 먼저 수강해주세요!", "status": 401}
        link = lectures.find_one({"order": order})["lecture_id"]
        seen = user["seen"]
        seen.append(order)
        lectures.update_one({"lecture_id": link}, {"$set": {"seen": True}})
        users.update_one({"uuid": user_id}, {"$set": user})
        return {"message": "success", "lecture_id": link}


@bp.route('/lecture', methods=['GET', 'POST'])
def show_lecture():
    if request.method == 'GET':
        lecture_id = request.args.get("id")
        user_id = request.cookies.get("username")
        user = users.find_one({"uuid": user_id})
        user["seen"].append(lecture_id)
        users.update_one({"uuid": user_id}, {"$set": user})
        lecture = lectures.find_one({"lecture_id": lecture_id})
        order = lecture["order"]
        next_lecture = lectures.find_one({"order": order+1})["lecture_id"]
        return {"message": "success", "lecture_id": next_lecture}
    elif request.method == "POST":
        user_id = request.cookies.get("username")
        course_name = request.cookies.get('course')
        print(request.base_url)
        body = json.loads(request.data.decode())
        order = body["order"]
        user = users.find_one({"uuid": user_id})
        courses_list = user['courses']
        if course_name not in courses_list:
            print("you didn't pay for that...")
            return {"message": "올바르지 않은 접근입니다.", "status": 401}
        if order != 1:
            if order-1 not in user["seen"]:
                return {"message": "앞에 강의를 먼저 수강해주세요!", "status": 401}
        return

