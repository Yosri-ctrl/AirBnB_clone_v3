#!/usr/bin/python3
"""_"""
from api.v1.views.index import *
from os import getenv
app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
