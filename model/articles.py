from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute
import os
from .meta import BaseModel

class ArticleModel(BaseModel):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = 'articles'
        region = 'us-east-2'
        aws_access_key_id=os.environ['aws_access_key_id']
        aws_secret_access_key=os.environ['aws_secret_access_key']

    id = UnicodeAttribute(hash_key=True)
    title = UnicodeAttribute(range_key=True)
    category = UnicodeAttribute()
    content = UnicodeAttribute()
    create_time = UnicodeAttribute()
    editor = UnicodeAttribute()
