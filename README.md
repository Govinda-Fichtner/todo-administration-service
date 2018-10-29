# todo-administration-service
Administration Microservice for ToDo App

## Run the API locally

1. Install `node`
2. run `npm install` to install all the packages, especially [`osprey-mock-service`](https://github.com/mulesoft-labs/osprey-mock-service)
3. run `npx osprey-mock-service -f api.raml -p 3000 --cors`

This will run an instance of `osprey-mock-service` on port 3000 using the RAML definition `api.raml`


## Pre-commit

1. Documentation of [`pre-commit`](https://pre-commit.com/)
2. `brew install pre-commit` or `pip install pre-commit` (also in the requirements-dev.txt)
3. For an initial local run - run `pre-commit run --all-files`.
4. Run `pre-commit install` to install pre-commit into your git hooks. pre-commit will now run on every commit. Every time you clone a project using pre-commit running `pre-commit install` should always be the first thing you do.

If you want to manually run all pre-commit hooks on a repository, run `pre-commit run --all-files`. To run individual hooks use pre-commit run <hook_id>.

The first time pre-commit runs on a file it will automatically download, install, and run the hook. Note that running a hook for the first time may be slow. For example: If the machine does not have node installed, pre-commit will download and build a copy of node.
