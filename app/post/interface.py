from datetime import datetime

from mypy_extensions import TypedDict


class PostInterface(TypedDict, total=False):
    """Post interface."""
    post_id: int
    title: str
    date_posted: datetime
    content: str
