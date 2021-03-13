from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return '<h1>Hello World!</h1>'


@app.route('/', methods=['GET'])
def index():
    return "main called"



@app.route('/dinz', methods=['GET'])
def dinz():
    return "Nithz!!"

if __name__ == '__main__':
    app.run()