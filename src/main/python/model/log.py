#   Date: 2018-08-12
#   Author: Lucas Nadalete
#
#   License: GPL v3


"""
    Log model used to mapping all fields of the table LOG_LOG.
"""

from model.base import Base
from webapp import db


class Log(Base):
    __tablename__ = 'log_log'
    __table_args__ = dict(extend_existing=True)

    user_name = db.Column('user_name', db.String(100), nullable=True)
    source_host = db.Column('source_host', db.String(200), nullable=True)
    target_host = db.Column('target_host', db.String(200), nullable=True)
    api_url = db.Column('api_url', db.String(1000), nullable=True)

    def __init__(self, un, sh, th, au, cdt):
        super(Log, self).__init__(cdt)
        self.user_name = un
        self.source_host = sh
        self.target_host = th
        self.api_url = au

    def __repr__(self):
        return '<Id {} - User Name {}>'.format(self.id, self.user_name)
