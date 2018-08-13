#   Date: 2018-07-10
#   Author: Lucas Nadalete
#
#   License: GPL v3


"""
    Controller class used to get the log registers persisted and save
    a new log register.
"""

from flask_restful import Resource, abort

from mapper.log_mapper import LogMapper
from repository.log_repository import LogRepository


class LogController(Resource):

    def get(self):
        logs = LogRepository.get_all()
        if len(logs) == 0:
            abort(404, message='No logs registered in database.')
        else:
            response = LogMapper.map_list_to_dic(logs)
            return response, 200

    def post(self):
        pass
