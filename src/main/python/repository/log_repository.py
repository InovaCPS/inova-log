#   Date: 2018-08-12
#   Author: Lucas Nadalete
#
#   License: GPL v3


"""
    Repository used to execute all CRUD operations of the
    Log entity
"""

from sqlalchemy.exc import SQLAlchemyError

from model.log import Log
from webapp import db


class LogRepository:

    @staticmethod
    def save(data):
        if data is not None:
            entity = Log(un=data['user_name'],
                         th=data['target_host'],
                         sh=data['source_host'],
                         cdt=data['created_datetime'],
                         au=data['api_url'],
                         )
            db.session.add(entity)
            try:
                db.session.commit()
            except SQLAlchemyError:
                return None
            return entity.id

    @staticmethod
    def get_all():
        return Log.query.all()

    @staticmethod
    def get_by_id(log_id):
        return Log.query.filter_by(id=log_id).first()
