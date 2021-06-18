from datetime import datetime

from pytest import fixture

from .interface import PostInterface
from .model import Post
from .schema import PostSchema


@fixture()
def schema() -> PostSchema:
    return PostSchema()


def test_PostSchema_create(schema: PostSchema):
    assert schema


def test_PostSchema_work(schema: PostSchema):
    param: PostInterface = schema.load({
        "postId": "12",
        "title": "test one",
        "datePosted": "2021-06-17 16:00:00",
        "content": "some test content"
    }).data
    post = Post(**param)

    assert post.post_id == 12
    assert post.title == "test one"
    assert post.date_posted == datetime(2021, 6, 17, 16, 0, 0)
    assert post.content == "some test content"
