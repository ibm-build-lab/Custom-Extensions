from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify, render_template, send_from_directory
from marshmallow import Schema, fields
from werkzeug.utils import secure_filename

PORT = 5000

app = Flask(__name__, template_folder='./swagger/templates')

spec = APISpec(
    title='flask-api-swagger-doc',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

@app.route('/api/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())

@app.route("/docs")

@app.route("/docs/<path:path>")
def swagger_docs(path=None):
    if not path or path == 'index.html':
        return render_template('index.html', base_url='/docs')
    else:
        return send_from_directory('./swagger/static', secure_filename(path))

# Marshmallow support
class LanguageResponseSchema(Schema):
    language = fields.Str()

class LanguageResponse(Schema):
    language_list = fields.List(fields.Nested(LanguageResponseSchema))

@app.route("/")
def home():
    return jsonify({"status": "online"})

@app.route("/languages")
def get_languages():
    """Get list of languages
    ---
    get:
        description: Get list of languages
        responses:
            200:
                description: Return a language list
                content:
                    application/json:
                        schema: LanguageResponse
    """

    languages = [
        {"language": "English"},
        {"language": "Spanish"},
        {"language": "French"},
        {"language": "German"},
        {"language": "Italian"},
        {"language": "Portuguese"},
        {"language": "Swedish"}
    ]

    return LanguageResponse().dump({"language_list": languages})

# Register API
with app.test_request_context():
    spec.path(view=get_languages)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)