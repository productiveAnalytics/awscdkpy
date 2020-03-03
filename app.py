#!/usr/bin/env python3

from aws_cdk import core

from awscdkpy.awscdkpy_stack import AwscdkpyStack


app = core.App()
AwscdkpyStack(app, "awscdkpy")

app.synth()
