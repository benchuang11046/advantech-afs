import uuid, os, pytest
from dotenv import load_dotenv
from tests.mock_requests import MockResponse


@pytest.fixture(scope='session')
def v1_env():
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path=env_path)

@pytest.fixture()
def test():
    return uuid.uuid4()

@pytest.fixture(scope='session')
def data_dir():
    yield os.path.join(os.path.dirname(__file__), 'data')

@pytest.fixture(scope='class')
def models_resource():
    from afs import models
    afs_models=models()
    yield afs_models

@pytest.fixture(scope='class')
def services_resource():
    from afs import services
    afs_services=services()
    yield afs_services

@pytest.fixture(scope='function')
def config_handler_resource():
    from afs import config_handler
    afs_config_handler = config_handler()
    yield afs_config_handler

@pytest.fixture(scope='class')
def conf_resource():
    conf={ "model_name":"test_model.h5"}
    return conf

@pytest.fixture(scope='session')
def client_session():
    from afs.client import EIPaaSAFSSession
    yield EIPaaSAFSSession()

@pytest.fixture(scope='function')
def mock_api_v2_resource(mocker):
    import requests
    mocker.patch.dict(os.environ, {
        'afs_url': 'http://afs.org.tw',
        'instance_id': '1234-4567-7890',
        'auth_code': '1234',
        'version': '2.0.2'}
    )
    mocker.patch.object(requests, 'get',
                        return_value=MockResponse(text="""{"API_version":"v2", "AFS_version":"2.0.2"}""",
                                     status_code=200)
                        )

@pytest.fixture(scope='function')
def mock_api_v1_resource(mocker):
    import requests
    mocker.patch.dict(os.environ, {
        'afs_url': 'http://afs.org.tw',
        'instance_id': '1234-4567-7890',
        'auth_code': '1234',
        'version': '1.2.29'}
    )
    mocker.patch.object(requests, 'get',
                        return_value=MockResponse(text="""{"API_version":"v1", "AFS_version":"1.2.29"}""",
                                     status_code=200)
                        )

@pytest.fixture(scope='function')
def mock_models(mocker):
    from afs import models
    yield models()

@pytest.fixture()
def model_name(test):
    test_model = 'test_model.h5'
    if os.path.exists(test_model):
        os.remove(test_model)
    with open(test_model, 'w') as f:
        f.write(str(test))
    yield test_model
    os.remove(test_model)

@pytest.fixture(scope='function')
def utils_resource():
    from afs import utils
    yield utils