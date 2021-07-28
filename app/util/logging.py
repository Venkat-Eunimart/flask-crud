from flask import request
import logging
from app import app
logging.basicConfig(filename='test.log', level=logging.DEBUG)

@app.after_request
def after_request_callback(response):
    response_value = response.get_data()
    app.logger.debug(response_value.decode("utf-8"))
    return response


@app.before_request
def before_request_callback():
    body = request.get_json(force=True)
    param = request.args.to_dict()
    app.logger.debug({'param': param, 'body': body})
