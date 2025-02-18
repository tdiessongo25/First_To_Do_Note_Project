from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from todo_app.config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    
    # Initialize MongoDB with retry logic
    try:
        mongo.init_app(app)
    except Exception as e:
        app.logger.error(f"Failed to initialize MongoDB: {e}")
        raise
    
    # Register blueprints
    from todo_app.routes.todo_routes import todos
    app.register_blueprint(todos)
    
    return app 