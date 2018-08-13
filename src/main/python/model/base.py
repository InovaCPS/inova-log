#   Date: 2018-08-12
#   Author: Lucas Nadalete
#
#   License: GPL v3


"""
    Base model used to mapping ID and CREATED_DATETIME fields.
"""

from webapp import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column('id', db.Integer, primary_key=True)
    created_datetime = db.Column('created_datetime', db.DateTime(), nullable=True)

    def __init__(self, cdt):
        self.created_datetime = cdt