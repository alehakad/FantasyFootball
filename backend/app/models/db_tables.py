from mongoengine import Document, StringField, IntField, ReferenceField


class Team(Document):
    name = StringField(required=True)


class Player(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    age = IntField()
    team = ReferenceField(Team)


class User(Document):
    username = StringField(required=True)
    email = StringField(required=True)
