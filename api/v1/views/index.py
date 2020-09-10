#!/usr/bin/python3
"""_"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def app_status():
    """return a JSON status=OK"""
    return(jsonify(status="OK"))
