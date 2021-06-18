from datetime import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy

from .interface import PostInterface
from .model import Post
from .service import PostService


def test_get_all(db: SQLAlchemy):
    tpost: Post = Post(post_id=12,
                       title='test one',
                       date_posted=datetime(2021, 6, 17, 16, 0, 0),
                       content='some test content')

    tspost: Post = Post(post_id=15,
                        title='test two',
                        date_posted=datetime(2021, 6, 17, 16, 0, 1),
                        content='some other test content')

    db.session.add(tpost)
    db.session.add(tspost)
    db.session.commit()

    results: List[Post] = PostService.get_all()

    assert len(results) == 2
    assert tpost in results and tspost in results


def test_update(db: SQLAlchemy):
    tpost: Post = Post(post_id=12,
                       title='test one',
                       date_posted=datetime(2021, 6, 17, 16, 0, 0),
                       content='some test content')

    db.session.add(tpost)
    db.session.commit()
    updates: PostInterface = dict(title='New Post title')

    PostService.update(tpost, updates)

    result: Post = Post.query.get(tpost.post_id)
    assert result.title == 'New Post title'


def test_delete_by_id(db: SQLAlchemy):  # noqa
    tpost: Post = Post(post_id=12,
                       title='test one',
                       date_posted=datetime(2021, 6, 17, 16, 0, 0),
                       content='some test content')
    tspost: Post = Post(post_id=15,
                        title='test two',
                        date_posted=datetime(2021, 6, 17, 16, 0, 1),
                        content='some other test content')
    db.session.add(tpost)
    db.session.add(tspost)
    db.session.commit()

    PostService.delete_by_id(12)
    db.session.commit()

    results: List[Post] = Post.query.all()

    assert len(results) == 1
    assert tpost not in results and tspost in results


def test_create(db: SQLAlchemy):
    tpost: PostInterface = dict(post_id=12,
                                title='test one',
                                date_posted=datetime(2021, 6, 17, 16, 0, 0),
                                content='some test content')
    PostService.create(tpost)
    res: List[Post] = Post.query.all()

    assert len(res) == 1

    for key in tpost.keys():
        assert getattr(res[0], key) == tpost[key]
