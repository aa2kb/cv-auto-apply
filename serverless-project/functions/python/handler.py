import json

def hello(event, context):
    body = {
        "message": "Hello from Python Function!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
