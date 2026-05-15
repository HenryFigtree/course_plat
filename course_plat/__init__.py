import os

from flask import Flask

#Create app
def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
            SECRET_KEY = os.environ.get("SECRET_KEY", "dev"),
            DATABASE = os.path.join(app.instance_path, 'course_plat.sqlite'),
            UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads'),
            ALLOWED_EXTENSIONS = {'pdf', 'ppt', 'pptx'}
    )
    
    #Load instance config if there is one
    if test_config is None:
        app.config.from_pyfile('config.py', silent = True)
    
    #Load test config if passed in
    else:
        app.config.from_mapping(test_config)

    #Ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok = True)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok = True)

    from . import db
    db.init_app(app)

    from . import admin
    app.register_blueprint(admin.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import courses
    app.register_blueprint(courses.bp)
    app.add_url_rule('/', endpoint = 'index')

    return app

