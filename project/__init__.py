from flask import Flask

app = Flask(__name__)

from project.api.users.views import users
from project.api.roles.views import role

app.register_blueprint(api.users.views.users)
app.register_blueprint(api.roles.views.role)