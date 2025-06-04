import redis
import pytest

@pytest.fixture
def server():
    return "controller.local"

@pytest.fixture
def port():
    return 6379

@pytest.fixture
def connect( server , port ):
    return redis.Redis(host=server, port=port, decode_responses=True)

def test_connection( connect ):
#    with pytest.raises(Exception) as e_info:
         connect.ping() 
