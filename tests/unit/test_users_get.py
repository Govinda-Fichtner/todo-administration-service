from hamcrest import assert_that, equal_to
from lib.users_get import handler

def test_users_get():
    event = {}
    context = {}

    response = handler(event, context)

    assert_that(response['statusCode'], equal_to(200))
