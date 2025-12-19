from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

#create a database instance(object of SQLAlchemy) globally
db = SQLAlchemy()

#function to create and configure the falsk application
def create_app():
    app = Flask(__name__)

    #create a secrete key for the application
    app.config['SECRET_KEY'] = 'my-secrete-key'
    app.config["WTF_CSRF_ENABLED"] = True #hackers ko rokne ke liye, wahi submit karenge jinke pas CSRF toke hoga
    #configure the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    #disable track modifications to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #initialize the database with the app, basically bind the database to the app
    db.init_app(app)
    # db.init_(app)
    # db.init_app(app)

    #register blueprints, by importing the blueprints from their respective modules
    from app.routes.auth import auth_bp#importing auth blueprint
    from app.routes.tasks import tasks_bp#importing tasks blueprint
    app.register_blueprint(auth_bp) #registering the auth blueprint
    app.register_blueprint(tasks_bp) #registering the tasks blueprint

    #ab finaly return the app instance
    return app