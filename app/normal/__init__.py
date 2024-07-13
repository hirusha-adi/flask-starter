from flask import Blueprint

normal = Blueprint('normal', __name__)

from app.normal import routes
