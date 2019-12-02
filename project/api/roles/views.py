from flask import Blueprint,request
import datetime
from .models import Role
from project.config import client

role = Blueprint('role',__name__)

@role.route("/role",methods=['POST'])
def create_role():
    role_name = request.json['role_name']

    role = Role(role_name = role_name,created_date = datetime.datetime.now())
    role_inserted = role.save()
    if role_inserted:
        return "Role Inserted"
    else:
        return "Insertion failed"

@role.route("/role",methods=['GET'])
def get_role():
    queryset = Role.objects()
    print(queryset)
    return queryset.to_json()

@role.route("/role/<uid>",methods=['PUT'])
def update_role(uid):
    update_role_name = request.json['role_name']
    role = Role.objects(pk = uid).get()
    role.role_name = update_role_name
    role_updated=role.save()
    if role_updated:
        return "updated role"