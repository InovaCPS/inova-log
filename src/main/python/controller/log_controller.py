#   Date: 2018-07-10
#   Author: Lucas Nadalete
#
#   License here! Copyright?


"""
    Controller class used to get the log registers persisted and save
    a new log register.
"""
from datetime import datetime

from flask_restful import Resource


class LogController(Resource):

    def get(self):
        response = {'message': 'Log queried with success'}
        response['system'] = 'pyetl-inova'
        response['source_host'] = '172.45.67.89'
        response['target_host'] = '192.168.9.2'
        response['datetime'] = str(datetime.now())
        return response, 200

    def post(self):
        pass
