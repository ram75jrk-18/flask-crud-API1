from flask import jsonify
from werkzeug.exceptions import HTTPException


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return jsonify({
            "status": "error",
            "message": error.description,
            "code": error.code
        }), error.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        app.logger.exception("Unhandled exception: %s", error)
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred.",
            "code": 500
        }), 500
