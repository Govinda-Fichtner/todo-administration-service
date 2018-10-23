# todo-administration-service
Administration Microservice for ToDo App

## Run the API locally

1. Install `node`
2. run `npm install` to install all the packages, especially [`osprey-mock-service`](https://github.com/mulesoft-labs/osprey-mock-service)
3. run `npx osprey-mock-service -f api.raml -p 3000 --cors`

This will run an instance of `osprey-mock-service` on port 3000 using the RAML definition `api.raml`
