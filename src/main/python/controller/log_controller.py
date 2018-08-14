#   Date: 2018-07-10
#   Author: Lucas Nadalete
#
#   License: GPL v3


"""
    Controller class used to get the log registers persisted and save
    a new log register.
"""

from flask import request, json
from flask_restful import Resource, abort

from basic_auth import requires_auth
from mapper.log_mapper import LogMapper
from repository.log_repository import LogRepository
from webapp import api, app


@api.resource('/log')
class LogController(Resource):

    @requires_auth
    def get(self):
        logs = LogRepository.get_all()
        if len(logs) == 0:
            abort(404, message='No logs registered in database.')
        else:
            response = app.response_class(
                response=json.dumps(LogMapper.map_list_to_dict(logs)),
                status=200,
                mimetype='application/json'
            )
            return response

    @requires_auth
    def post(self):
        json_data = request.get_json(force=True)
        entity = LogRepository.save(json_data)
        if entity is not None:
            response = app.response_class(
                response=json.dumps(LogMapper.map_entity_to_dict(entity)),
                status=201,
                mimetype='application/json'
            )
            return response
        else:
            abort(422, message='Fail to process log request.')
