import collections
from sqlalchemy.inspection import inspect
from datetime import datetime, date
from dateutil.tz import tzlocal

class Serializer(object):

    def serialize(self):
        dic = {}
        for k in inspect(self).attrs.keys():
            val = getattr(self, k)
            
            if isinstance(val, Serializer):
                val = val.serialize()
            elif isinstance(val, datetime):
                val = val.replace(tzinfo=tzlocal()).isoformat()
            elif isinstance(val, date):
                val = val.isoformat()
            elif isinstance(val, collections.Sequence) and not isinstance(val, str):
                val = Serializer.serialize_list(val)

            dic[k] = val
        return dic

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

