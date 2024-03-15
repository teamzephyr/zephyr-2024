from flask import Flask, request, abort

app = Flask(__name__) 

# swagger.apispecs({
#     "thisFile":"does it show"
# })

from endpoints import *
# api = Api(app, version='3.0.0', title='esgBenchmark Service', description="esgBenchmark service using saggger ui", doc='/swagger')

# app.register_blueprint(index)
# app.register_blueprint(flaskDemo)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)