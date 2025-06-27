from flask import Flask
# from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from myapp.configuration import Config

app = Flask(__name__)

# load the settings from the configuration file
app.config.from_object(Config)
# CORS(app, resources={r"/api/*": {"origins": "*"}})  # Enable CORS for all routes

from myapp.public import public_model, public_views
from myapp.article import article_views, article_model