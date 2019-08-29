from pynamodb.models import Model
import json

class BaseModel(Model):

    def to_dict(self):
        rval = {}
        for key in self.attribute_values:
            rval[key] = self.__getattribute__(key)
        return rval
