from datetime import datetime

from pytest import fixture

from .model import Post


@fixture()
def post() -> Post:
    return Post(
        post_id=12,
        title='test one',
        date_posted=datetime(2021, 6, 17, 16, 0, 0),
        content='some test content',
    )


def test_Post_create(post: Post):
    assert post
