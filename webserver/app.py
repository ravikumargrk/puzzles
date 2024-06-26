from flask import Flask
from flask_restful import Resource, Api, request

from datetime import datetime
import os
os.chdir(r'/workspaces/puzzles/webserver/data/')

import subprocess

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'doc': 'this is a test server for academic purposes'}
    
    def post(self):
        data = request.get_data()
        dt = datetime.now().isoformat().replace(':','-')
        path = request.headers.get('filename')
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
        return path

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)