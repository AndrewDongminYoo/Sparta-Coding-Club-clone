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
