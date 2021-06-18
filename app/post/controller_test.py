from datetime import datetime
from unittest.mock import patch

from flask.testing import FlaskClient

from app.test.fixtures import client, app  # noqa
from . import BASE_ROUTE
from .interface import PostInterface
from .model import Post
from .schema import PostSchema
from .service import PostService


def make_post(
        post_id: int = 12,
        title: str = 'test one',
        date_posted: datetime = datetime(2021, 6, 17, 16, 0, 0),
        content: str = 'some test content'
) -> Post:
    return Post(post_id=post_id,
                title=title,
                date_posted=date_posted,
                content=content)


class TestPostResource:
    @patch.object(
        PostService,
        "get_all",
        lambda: [
            make_post(12, title="Test Post 1"),
            make_post(15, title="Test Post 2"),
        ],
    )
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                PostSchema(many=True).dump(
                    [
                        make_post(12, title="Test Post 1"),
                        make_post(15, title="Test Post 2"),
                    ]
                )

            )
            for r in results:
                assert r in expected

    @patch.object(
        PostService, "create", lambda create_request: Post(**create_request)
    )
    def test_post(self, client: FlaskClient):  # noqa
        with client:
            payload = dict(title="Test post", content="Test content")
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                PostSchema().dump(Post(title=payload["title"], content=payload["content"]))

            )
            assert result == expected


def fake_update(post: Post, changes: PostInterface) -> Post:
    # To fake an update, just return a new object
    updated_Post = Post(
        post_id=post.post_id, title=changes["title"], content=changes["content"]
    )
    return updated_Post


class TestPostIdResource:
    @patch.object(PostService, "get_by_id", lambda id: make_post(post_id=id))
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/12").get_json()
            expected = make_post(post_id=12)
            print(f"result = ", result)
            assert result["postId"] == expected.post_id

    @patch.object(PostService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):  # noqa
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/12").get_json()
            expected = dict(status="Success", id=12)
            assert result == expected

    @patch.object(PostService, "get_by_id", lambda id: make_post(post_id=id))
    @patch.object(PostService, "update", fake_update)
    def test_put(self, client: FlaskClient):  # noqa
        with client:
            result = client.put(
                f"/api/{BASE_ROUTE}/12",
                json={"title": "New Post", "content": "New content"},
            ).get_json()
            expected = (
                PostSchema().dump(Post(post_id=12,
                                       title='test one',
                                       date_posted=datetime(2021, 6, 17, 16, 0, 0),
                                       content='some test content'))

            )
            assert result == expected
