#   Date: 2018-07-10
#   Author: Lucas Nadalete
#
#   License here! Copyright?


"""
    This module provides a flask application responding
    to the endpoints of Logger.
"""

from flask import Flask
from flask_restful import Api

from controller.log_controller import LogController

app = Flask(__name__)
api = Api(app)

api.add_resource(LogController, '/log')
