from behave import fixture
from behave import use_fixture
from fastapi.testclient import TestClient

from infrastructure.adapters.rest.main import app


@fixture
def fastapi_client(context, *args, **kwargs):
    context.client = TestClient(app)
    yield context.client


def before_feature(context, feature):
    use_fixture(fastapi_client, context)
