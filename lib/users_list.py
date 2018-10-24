import json


def handler(event, context):
  users = [{"name": "Peter", "age": "30", "email": "peter.mueller@gmail.com"}, {
      "name": "Martina", "age": "32", "email": "martina.brot@gmail.com"}]
  response = {
      "statusCode": 200,
      "body": json.dumps(users)
  }

  return response
