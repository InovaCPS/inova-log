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
from flask_sqlalchemy import SQLAlchemy

from helper.config_helper import ConfigHelper


def config_db_url(resource):
    config = ConfigHelper(resource)
    url = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(
        db=config.get_property_by_section('datasource', 'inova.db.datasource'),
        host=config.get_property_by_section('datasource', 'inova.db.host'),
        port=config.get_property_by_section('datasource', 'inova.db.port'),
        user=config.get_property_by_section('datasource', 'inova.db.username'),
        pw=config.get_property_by_section('datasource', 'inova.db.password')
    )
    return url


def get_db_instance(app, db_url):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return SQLAlchemy(app)


APP_RESOURCE = './src/main/resources/application.properties'
DB_URL = config_db_url(APP_RESOURCE)
app = Flask(__name__)
api = Api(app)
db = get_db_instance(app, DB_URL)

from controller.log_controller import LogController

api.add_resource(LogController, '/log')
