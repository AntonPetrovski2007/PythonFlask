from flask import Flask
from config import Configuration
from posts.blueprint import posts
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object(Configuration)
db = SQLAlchemy(application)

application.register_blueprint(posts, url_prefix="/blog")
