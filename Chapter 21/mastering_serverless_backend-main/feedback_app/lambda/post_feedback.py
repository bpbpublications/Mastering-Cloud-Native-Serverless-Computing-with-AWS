import json
import uuid
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    body = json.loads(event['body'])
    feedback = {
        'id': str(uuid.uuid4()),
        'name': body.get('name'),
        'email': body.get('email'),
        'message': body.get('message')
    }
    table.put_item(Item=feedback)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': '*'
        },
        'body': json.dumps(feedback)
    }
