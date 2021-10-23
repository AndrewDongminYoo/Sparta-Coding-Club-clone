# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from application import application


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
        pass


@application.route('/api/lecture', methods=['GET', 'POST'])
def show_lecture():
    if request.method == 'GET':
        pass
    elif request.method == "POST":
        pass
