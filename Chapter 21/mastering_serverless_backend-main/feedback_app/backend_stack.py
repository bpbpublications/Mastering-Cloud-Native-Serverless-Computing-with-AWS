from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    aws_dynamodb as ddb,
)
from constructs import Construct
import os

class  BackendStack (Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # DynamoDB Table
        table = ddb.Table(
            self, "FeedbackTable",
            partition_key={"name": "id", "type": ddb.AttributeType.STRING}
        )

        # Common Lambda properties
        lambda_props = {
            "runtime": _lambda.Runtime.PYTHON_3_11,
            "environment": {"TABLE_NAME": table.table_name},
        }

        # POST Lambda
        post_fn = _lambda.Function(
            self, "PostFeedbackFunction",
            handler="post_feedback.lambda_handler",
            code=_lambda.Code.from_asset("feedback_app/lambda"),
            **lambda_props
        )

        # GET Lambda
        get_fn = _lambda.Function(
            self, "GetFeedbackFunction",
            handler="get_feedback.lambda_handler",
            code=_lambda.Code.from_asset("feedback_app/lambda"),
            **lambda_props
        )

        # DELETE Lambda
        delete_fn = _lambda.Function(
            self, "DeleteFeedbackFunction",
            handler="delete_feedback.lambda_handler",
            code=_lambda.Code.from_asset("feedback_app/lambda"),
            **lambda_props
        )

        # Grant access to DynamoDB
        table.grant_read_write_data(post_fn)
        table.grant_read_data(get_fn)
        table.grant_write_data(delete_fn)

        # API Gateway
        api = apigw.RestApi(self, "FeedbackApi", rest_api_name="Feedback Service")

        feedback_resource = api.root.add_resource("feedback")
        feedback_resource.add_method("POST", apigw.LambdaIntegration(post_fn))
        feedback_resource.add_method("GET", apigw.LambdaIntegration(get_fn))
        
        feedback_resource.add_cors_preflight(
            allow_origins=["*"],
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["*"]
        )

        item_resource = feedback_resource.add_resource("{id}")
        item_resource.add_method("DELETE", apigw.LambdaIntegration(delete_fn))
