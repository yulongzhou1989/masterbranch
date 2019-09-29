from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import os
from .meta import BaseModel

class WishModel(BaseModel):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = 'wishes'
        region = 'us-east-2'
        aws_access_key_id=os.environ['aws_access_key_id']
        aws_secret_access_key=os.environ['aws_secret_access_key']


    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute()
    content = UnicodeAttribute()
    priority = UnicodeAttribute()
    status = UnicodeAttribute()
    timespend = UnicodeAttribute()
    create_time = UnicodeAttribute()
    parent_wish_id = UnicodeAttribute(null=True)
    finish_time = UnicodeAttribute(null=True)
    real_time_cost = UnicodeAttribute(null=True)


    def __lt__(self, other):
        if (self.priority == other.priority):
            return other.timespend > self.timespend if self.timespend != other.timespend else other.create_time < self.create_time
        else:
            return other.priority > self.priority
