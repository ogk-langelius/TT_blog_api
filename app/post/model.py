from app import db
from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime, Text

from .interface import PostInterface


class Post(db.Model):
    """Post model."""

    __tablename__ = 'post'

    post_id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    date_posted = Column(DateTime(), nullable=False, default=datetime.utcnow)
    content = Column(Text(), nullable=False)

    def update(self, changes: PostInterface):
        for column, value in changes.items():
            setattr(self, column, value)
        return self
