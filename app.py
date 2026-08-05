import json
from datetime import datetime

def lambda_handler(event, context):

    print("===================================")
    print("Docker Lambda Application")
    print("Version : 1")
    print("Execution Time :", datetime.now())
    print("===================================")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Docker Lambda Executed Successfullyiiiii",
            "time": str(datetime.now())
        })
    }