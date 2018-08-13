#   Date: 2018-08-12
#   Author: Lucas Nadalete
#
#   License: GPL v3


"""
    Mapper used to convert:
     - Entity to Dict
     - List<Entity> to List<Dict>
"""

from datetime import datetime

class LogMapper:

    @staticmethod
    def map_entity_to_dict(entity):
        fmt = '%Y-%m-%d %H:%M:%S'
        log = {'id': entity.id,
               'user_name': entity.user_name,
               'created_datetime': entity.created_datetime.strftime(fmt),
               'source_host': entity.source_host,
               'target_host': entity.target_host,
               'api_url': entity.api_url
               }
        return log

    @staticmethod
    def map_list_to_dic(entities):
        logs = []
        for entity in entities:
            logs.append(LogMapper.map_entity_to_dict(entity))
        return logs
