from marshmallow import fields, Schema


class PostSchema(Schema):
    """Post schema."""
    postId = fields.Number(attribute='post_id')
    title = fields.String(attribute='title')
    datePosted = fields.DateTime(attribute='date_posted')
    content = fields.String(attribute='content')
