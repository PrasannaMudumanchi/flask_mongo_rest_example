from flask import Blueprint,request
from .models import User
from project.config import client

users = Blueprint('users',__name__)

@users.route("/users", methods=['POST'])
def create_user():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone']
    role = request.json['role']

    user = User(first_name=first_name,last_name=last_name,phone=phone,role = role)
    user_inserted=user.save()
    print(user.role.role_name)
    # role_user = Role.objects(pk=role).get()
    # print(user_inserted)
    # role_inserted = role_user.users.append(user_inserted)
    # print(user_inserted)
    # role_inserted.save()
    # print(user_inserted)
    # print(role_user.id)
    # print(role_inserted)
    if user_inserted:
        return "User Inserted"
    else:
        return "Error in User insertion"

@users.route("/users", methods=['GET'])
def get_users():
    queryset = User.objects()
    for user in queryset:
        print(user.role.role_name)
    return queryset.to_json()