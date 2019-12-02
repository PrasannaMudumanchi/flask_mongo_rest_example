from mongoengine import *

class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone = StringField(max_length=10)
    role = ReferenceField('Role')