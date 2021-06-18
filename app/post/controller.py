from typing import List

from flask import request
from flask.wrappers import Response
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from .interface import PostInterface
from .model import Post
from .schema import PostSchema
from .service import PostService

api = Namespace('Post', description='Namespace for post')


@api.route('/')
class PostResource(Resource):
    """Posts."""

    @responds(schema=PostSchema, many=True)
    def get(self) -> List[Post]:
        """Get all posts."""
        return PostService.get_all()

    @accepts(schema=PostSchema, api=api)
    @responds(schema=PostSchema)
    def post(self) -> Post:
        """Create single post."""
        return PostService.create(request.parsed_obj)


@api.route('/<int:postID>')
@api.param('postID', 'Post database ID')
class PostIDResource(Resource):
    """Single post operations."""
    @responds(schema=PostSchema)
    def get(self, postID: int) -> Post:
        """Get single post by ID."""
        return PostService.get_by_id(postID)

    def delete(self, postID: int) -> Response:
        """Delete single post by ID."""
        from flask import jsonify

        return jsonify(dict(status='Success', id=PostService.delete_by_id(postID)))

    @accepts(schema=PostSchema, api=api)
    @responds(schema=PostSchema)
    def put(self, postID: int) -> Post:
        """Update single post by ID."""
        changes: PostInterface = request.parsed_obj
        return PostService.update(PostService.get_by_id(postID), changes)
