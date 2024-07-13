from flask import Flask
from app.extensions import db, migrate, login_manager, sitemap, csrf
from app.views.main import main_bp
from app.views.admin import admin_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    sitemap.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app
