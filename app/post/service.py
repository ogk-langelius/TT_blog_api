from typing import List
from app import db

from .interface import PostInterface
from .model import Post


class PostService:
    @staticmethod
    def get_all() -> List[Post]:
        return Post.query.all()

    @staticmethod
    def get_by_id(post_id: int) -> Post:
        return Post.query.get(post_id)

    @staticmethod
    def update(post: Post, Post_change_updates: PostInterface) -> Post:
        post.update(Post_change_updates)
        db.session.commit()
        return post

    @staticmethod
    def delete_by_id(post_id: int) -> List[int]:
        post = Post.query.filter(Post.post_id == post_id).first()
        if not post:
            return []
        db.session.delete(post)
        db.session.commit()
        return [post_id]

    @staticmethod
    def create(new_attrs: PostInterface) -> Post:
        new_post = Post(title=new_attrs['title'], content=new_attrs['content'])

        db.session.add(new_post)
        db.session.commit()

        return new_post
