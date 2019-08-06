from boto3.dynamodb.conditions import Key, Attr
import boto3
import botocore
import os

class Database:

    @staticmethod
    def operate(tablename, action, exp):
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=os.environ['aws_access_key_id'],
            aws_secret_access_key=os.environ['aws_secret_access_key'],
            region_name=os.environ['region_name'])

        table = dynamodb.Table(tablename)
        if action == 'scan':
            response = table.scan(exp)

        print(response)
        return response
