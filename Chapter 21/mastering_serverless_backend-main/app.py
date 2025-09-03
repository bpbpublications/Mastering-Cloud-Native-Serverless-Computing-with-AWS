#!/usr/bin/env python3
import aws_cdk as cdk
from feedback_app.backend_stack import BackendStack

app = cdk.App()
BackendStack(app, "FeedbackBackendStack")
app.synth()
