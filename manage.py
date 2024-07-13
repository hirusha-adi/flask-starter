from flask import Flask
from flask.cli import FlaskGroup
from app import create_app
from app.extensions import db

def create_flask_app():
    return create_app()

cli = FlaskGroup(create_app=create_flask_app)

if __name__ == '__main__':
    cli()
