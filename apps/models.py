import mongoengine as me
from application import application
from flask_mongoengine import MongoEngine

application.config['MONGODB_SETTINGS'] = {
    "db": "Lecture",
    "port": 27017,
    "host": "localhost"
}
db = MongoEngine(application)
# me.register_connection(db=db)
# me.connect(db=db)


class Lecture(me.Document):
    title = me.StringField(required=True)
    done = me.BooleanField()
    seen = me.BooleanField()
    playtime = me.IntField()
    enrolled_detail_id = me.UUIDField()
    enrolled_id = me.UUIDField()
    lecture_id = me.UUIDField()
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


test_data = [
    {"title": "웹개발종합반", "tutor": "이범규", "price": 800000, "discount_ratio": 0.29, "week": 8},
    {"title": "리액트기초반", "tutor": "임민영", "price": 500000, "discount_ratio": 0.18, "week": 5},
    {"title": "스프링기초반", "tutor": "남병관", "price": 500000, "discount_ratio": 0.18, "week": 5},
]

if __name__ == '__main__':
    for data in test_data:
        doc = Course(
            title=data['title'],
            tutor=data['tutor'],
            week=data['week'],
            price=data['price'],
            discount_ratio=data['discount_ratio']
        )
        # db.courses.insert_one(doc.to_mongo())
