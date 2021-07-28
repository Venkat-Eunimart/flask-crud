from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_json_schema import JsonSchema, JsonValidationError
app = Flask(__name__)
db = SQLAlchemy(app)
schema = JsonSchema(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/database2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from app.util import logging
from app.routes import student,course

db = SQLAlchemy(app)

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({ 'Lerror': e.message,'errors': [validation_error.message for validation_error  in e.errors]})
