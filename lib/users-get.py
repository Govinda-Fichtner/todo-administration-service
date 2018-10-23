import json


def handler(event, context):
  users = {
      "username": "Martina", "id": "32", "email": "martina.brot@gmail.com"}
  response = {
      "statusCode": 200,
      "body": json.dumps(users)
  }

  return response
