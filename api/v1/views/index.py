#!/usr/bin/python3
"""_"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def app_status():
    """return a JSON status=OK"""
    return(jsonify(status="OK"))

@app_views.route('/stats')
def app_get_count():
    """
    Returns statistics about the number of objects available
    """
    tojson = {}
    for cls in storage.available_classes:
        string = str(cls).lower()
        if string[-1] is 'y':
            string = string[0:-1] + "ies"
        else:
            string += "s"
        tojson.update({string: storage.count(cls)})
    return(jsonify(tojson))
