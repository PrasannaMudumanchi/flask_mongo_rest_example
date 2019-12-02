from mongoengine import *

class Role(Document):
    role_name = StringField(max_length=50,required=True)
    users = ListField(ReferenceField('User',reverse_delete_rule=CASCADE))
    created_date = DateTimeField(required=True)
