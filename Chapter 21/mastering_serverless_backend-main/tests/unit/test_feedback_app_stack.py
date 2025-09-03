import aws_cdk as core
import aws_cdk.assertions as assertions

from feedback_app.feedback_app_stack import FeedbackAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in feedback_app/feedback_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FeedbackAppStack(app, "feedback-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
