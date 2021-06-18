def register_routes(api, app, root='api'):
    """Routes registration."""
    from app.post import register_routes as attach_post

    attach_post(api, app)
