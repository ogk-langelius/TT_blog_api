from datetime import datetime

from pytest import fixture

from .interface import PostInterface
from .model import Post


@fixture()
def interface() -> PostInterface:
    return PostInterface(
        post_id=12,
        title='test one',
        date_posted=datetime(2021, 6, 17, 16, 0, 0),
        content='some test content',
    )


def test_PostInterface_create(interface: PostInterface):
    assert interface


def test_PostInterface_work(interface: PostInterface):
    post = Post(**interface)
    assert post
