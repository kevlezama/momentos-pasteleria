# Flask framework
from flask import Flask
from flask_migrate import Migrate
#from flask_cors import CORS

# Global config dependencies
from app.dbconfig import db
from app.config import DevelopmentConfig as DEVCONFIG

# Routes
from .routes.main import main_bp

#Services
from .services.roles_services import roles_bp

# Models
import logging

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
FILE = "mp.log"

migrate = Migrate()

def create_app():

    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object(DEVCONFIG)

    """Initialize modeules."""
    #CORS(app)
    
    logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=FILE
    )

    app.register_blueprint(main_bp)
    app.register_blueprint(roles_bp)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Initialize Models
    from .models.client_model import Client
    from .models.addresses_model import Client_adress_model
    from .models.roles_model import RolesModel

    return app
