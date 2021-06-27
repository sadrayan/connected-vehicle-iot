# import greengrasssdk
import time
import json
from Helper import *
import boto3

# Greengrass client to publish to
# client = greengrasssdk.client('iot-data')
client = boto3.client("iot-data")
helper = Helper()

def handeler(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    # If the data comes from the cars
    # if event['device'] in ['benz-250', 'benz']:
    #     # Publish to the lab/greengrass/telemetry what was received
    #     print("publishing to lab/greengrass/telemetry  ", json.dumps(event) )
    #     client.publish(topic='lab/greengrass/telemetry', payload=json.dumps(event))
    # else:
    #     print ("Not a valid Vehicle")

    client.publish(topic='cvt/smartbox', payload=json.dumps(event))
    print(response)    
    print('calling servo')
    helper.test_Servo()

    return response

if __name__ == '__main__':
    handeler(json.dumps({'event' : 1}))