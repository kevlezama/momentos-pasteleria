from flask import Flask

# Global dependencies
from app.dbconfig import db
from app.config import DevelopmentConfig as DEVCONFIG

# Routes

from .routes.main import main_bp

def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object(DEVCONFIG)

    
    app.register_blueprint(main_bp)

    # Initialize Plugins
    db.init_app(app)

    return app
