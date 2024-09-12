from flask import Blueprint
from api.views.index import *

app_view = Blueprint('blueprint', __name__, url_prefix='/api')
