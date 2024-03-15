from flask import Flask, request, abort
from flasgger import Swagger

app = Flask(__name__) 
swagger = Swagger(app)

from endpoints import *
# app.register_blueprint(index)
# app.register_blueprint(flaskDemo)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)