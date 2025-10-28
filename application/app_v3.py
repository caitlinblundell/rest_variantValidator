"""
Simple rest interface for VariantVlidator built using Flask Flask-RESTX and Swagger UI
"""

# Import modules
from flask import Flask
from flask_restx import Api, Resource
import requests

# Define the application as a Flask app with the name defined by __name__ (i.e. the name of the current module)
# Most tutorials define application as "app", but I have had issues with this when it comes to deployment,
# so application is recommended
application = Flask(__name__)

# Define the API as api
api = Api(app = application)

# Define a name-space to be read Swagger UI which is built in to Flask-RESTX
# The first variable is the path of the namespace the second variable describes the space
hello_space = api.namespace('hello', description='Simple API that returns a greeting')
@hello_space.route("/")
class HelloClass(Resource):
    def get(self):
        return {
            "greeting": "Hello World"
        }


name_space = api.namespace('name', description='Return a name provided by the user')
@name_space.route("/<string:name>")
class NameClass(Resource):
    def get(self, name):
        return {
            "My name is" : name
        }

vv_space = api.namespace('VariantValidator', description='VariantValidator APIs')
@vv_space.route("/variantvalidator/<string:transcript_id>")
class VariantValidatorClass(Resource):
    def get(self, transcript_id):

        # Make a request to the curent VariantValidator rest-API
        url = "/".join(['https://rest.variantvalidator.org/VariantValidator/tools/gene2transcripts/', transcript_id]) # create url from parameters for api get request
        validation = requests.get(url) # use requests module to make request
        content = validation.json() # get the json content from the response
        return content

# Allows app to be run in debug mode
if __name__ == '__main__':
    application.debug = True # Enable debugging mode
    application.run(host="127.0.0.1", port=5000) # Specify a host and port fot the app