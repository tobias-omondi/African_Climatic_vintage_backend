from flask import Flask
from flask_restful import Resource, Api
from myapp import create_app

app = create_app()
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5500)
