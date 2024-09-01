import sys
import os
from flask import Flask
from flask_restful import Api
from apispec import APISpec
# from apispec.ext.flask import FlaskPlugin
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from app.routes import api_blueprint

# Ensure the 'app' module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)
app.register_blueprint(api_blueprint)
api = Api(app)

spec = APISpec(
    title="Example Microservice API",
    version="1.0.0",
    openapi_version="3.0.0",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

with app.test_request_context():
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            spec.path(view=app.view_functions[rule.endpoint])

# Save OpenAPI spec to a file
with open("openapi/openapi.yaml", "w") as f:
    f.write(spec.to_yaml())
