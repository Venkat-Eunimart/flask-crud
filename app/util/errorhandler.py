from flask import jsonify
def handle_error(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            return jsonify("error occured")
    wrapper.__name__=func.__name__
    return wrapper
