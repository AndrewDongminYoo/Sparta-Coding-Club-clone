# -*- coding: utf-8 -*-
import uuid
import mongoengine as me
from flask_login import UserMixin


class Lecture(me.Document):
    title = me.StringField(required=True)
    done = me.BooleanField()
    seen = me.BooleanField()
    playtime = me.IntField()
    enrolled_detail_id = me.UUIDField(binary=False)
    enrolled_id = me.UUIDField(binary=False)
    lecture_id = me.UUIDField(binary=False)
    order = me.IntField()
    course_title = me.StringField(required=True)
    week = me.IntField()
    week_order = me.IntField()
    link = me.URLField()


class Course(me.Document):
    price = me.IntField(required=True)
    discount_ratio = me.FloatField(required=True)
    title = me.StringField(max_length=32)
    tutor = me.StringField(min_length=2)
    week = me.IntField(min_value=1, max_value=18)


class User(me.Document, UserMixin):
    uuid = me.UUIDField(binary=False)
    username = me.StringField(max_length=32, unique=True)
    password = me.StringField(max_length=64)
    created_at = me.DateTimeField()
    done = me.ListField()
    seen = me.ListField()
    courses = me.ListField()

    def is_authenticated(self):
        super()

    def is_active(self):
        super()


if __name__ == '__main__':
    test_data = [
        {"title": "웹개발 종합반", "tutor": "이범규", "price": 800000, "discount_ratio": 0.29, "week": 8},
        {"title": "리액트 기초반", "tutor": "임민영", "price": 500000, "discount_ratio": 0.18, "week": 5},
        {"title": "스프링 기초반", "tutor": "남병관", "price": 500000, "discount_ratio": 0.18, "week": 5},
    ]
    for data in test_data:
        doc = Course(
            id=uuid.uuid4(),
            title=data['title'],
            tutor=data['tutor'],
            week=data['week'],
            price=data['price'],
            discount_ratio=data['discount_ratio']
        )
        # db.courses.insert_one(doc.to_mongo())
