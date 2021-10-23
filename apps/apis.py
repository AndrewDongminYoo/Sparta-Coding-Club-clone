# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from application import application


@application.route('/api/courses', methods=['GET', 'POST'])
def show_courses():
    if request.method == 'GET':
        # 유저에 따른 강의 목록 및 진도율 표기
        pass
    elif request.method == "POST":
        # 강의 페이지로 넘어가기 위한 유효성 검사
        pass


@application.route('/api/enrollment', methods=['GET', 'POST'])
def post_enrollment():
    if request.method == 'GET':
        # 설정한 강의의 정보를 화면에 전송해주는 API
        pass
    elif request.method == "POST":
        # 수강 신청을 접수하고 유효한지 확인한 후 디비에 저장 후 진도기록표로 리다이렉트
        pass


@application.route('/api/lecture', methods=['GET', 'POST'])
def show_lecture():
    if request.method == 'GET':
        # 강의의 회차 수 정보를 받아 디비에 있는 해당 주차 수업 영상 주소를 리턴
        pass
    elif request.method == "POST":
        # 강의를 다 보았을 때나 다른 강의로 넘어가려 할 때 가능한지 체크 후 리턴
        pass
