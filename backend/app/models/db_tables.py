from mongoengine import Document, StringField, IntField, ReferenceField
from db_connect import connect


class Team(Document):
    name = StringField(required=True)


class Player(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    age = IntField()
    team = ReferenceField(Team)

    meta = {"allow_inheritance": True}


class User(Document):
    username = StringField(required=True)
    email = StringField(required=True)


if __name__ == "__main__":
    user = User(username="ak", email="a@gmail.com").save()
    team = Team(name="River").save()
    player = Player(first_name="A", last_name="K", age=21, team=team).save()
