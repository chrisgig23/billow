from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Configuration setup
    app.config.from_object('app.config.Config')
    
    # Initialize database and migrations
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import and register routes
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app