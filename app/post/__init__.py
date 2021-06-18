from .model import Post
from .schema import PostSchema

BASE_ROUTE = 'post'


def register_routes(api, app, root='api'):
    """Routes registration."""
    from .controller import api as post_api

    api.add_namespace(post_api, path=f'/{root}/{BASE_ROUTE}')
