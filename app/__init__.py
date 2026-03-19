from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import Blueprints
    from app.routes.dashboard import dashboard_bp
    from app.routes.tasks import tasks_bp
    from app.routes.upload import upload_bp

    # Register Blueprints
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(upload_bp)

    return app