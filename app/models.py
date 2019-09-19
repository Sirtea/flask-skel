from flask_mongoengine import MongoEngine

db = MongoEngine()


# class Fruit(db.Document):
#     name = db.StringField()
#     meta = {'collection': 'fruits'}
