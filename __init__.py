from flask import Flask
from .extensions import db
from .errors import register_error_handlers
from .routes.items import items_bp


def create_app(config_object: str = "config.Config") -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    db.init_app(app)

    register_error_handlers(app)
    app.register_blueprint(items_bp, url_prefix="/api/items")

    @app.get("/")
    def home():
        return {
            "message": "Flask CRUD Mini Project API is running.",
            "docs": {
                "health": "/health",
                "items": "/api/items"
            }
        }, 200

    @app.get("/health")
    def health_check():
        return {"status": "success", "message": "API is healthy"}, 200

    with app.app_context():
        db.create_all()

    return app
