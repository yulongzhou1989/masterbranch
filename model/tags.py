from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute
import os
from .meta import BaseModel

class TagModel(BaseModel):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = 'tags'
        region = 'us-east-2'
        aws_access_key_id=os.environ['aws_access_key_id']
        aws_secret_access_key=os.environ['aws_secret_access_key']

    tag_name = UnicodeAttribute(hash_key=True)
