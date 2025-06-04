import redis
import pytest

@pytest.fixture
def server():
    return "controller.local"

@pytest.fixture
def port():
    return 6379

@pytest.fixture
def message():
    return "bar"

@pytest.fixture
def channel():
    return "foo"

@pytest.fixture
def connect( server , port ):
    return redis.Redis(host=server, port=port, decode_responses=True)

def test_connection( connect ):
#    with pytest.raises(Exception) as e_info:
         connect.ping() 

def test_write( connect , channel, message  ):
    connect.set( channel , message )

def test_read( connect , channel, message ):
    bar = connect.get( channel )
    assert bar ==  message

def test_destroy( connect , channel ):
    connect.delete( channel )
