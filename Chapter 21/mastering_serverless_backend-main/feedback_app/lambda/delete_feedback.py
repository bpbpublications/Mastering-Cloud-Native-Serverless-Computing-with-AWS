import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    feedback_id = event['pathParameters']['id']
    table.delete_item(Key={'id': feedback_id})
    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Feedback {feedback_id} deleted'})
    }
