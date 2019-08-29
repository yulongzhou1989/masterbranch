from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute
import os
from .meta import BaseModel

class CategoryModel(BaseModel):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = 'categories'
        region = 'us-east-2'
        aws_access_key_id=os.environ['aws_access_key_id']
        aws_secret_access_key=os.environ['aws_secret_access_key']

    category_name = UnicodeAttribute(hash_key=True)
    sub_category = ListAttribute()
