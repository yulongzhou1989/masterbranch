from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
import os

class UserModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = 'users'
        region = 'us-east-2'
        aws_access_key_id=os.environ['aws_access_key_id']
        aws_secret_access_key=os.environ['aws_secret_access_key']

    user_name = UnicodeAttribute(hash_key=True)
    user_passcode = UnicodeAttribute()
