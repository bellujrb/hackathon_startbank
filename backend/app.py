from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from routes.split import split_bp
from routes.transfer import transfer_bp
from routes.brcode_payment import brcode_payment_bp
from routes.tax_payment import tax_payment_bp
import starkbank
import config

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

starkbank.user = config.project

app.register_blueprint(split_bp, url_prefix='/v2/split')
app.register_blueprint(transfer_bp, url_prefix='/v2/transfer')
app.register_blueprint(brcode_payment_bp, url_prefix='/v2/brcode-payment')
app.register_blueprint(tax_payment_bp, url_prefix='/v2/tax-payment')

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "StarkBank API",
        "description": "API para interagir com o StarkBank",
        "version": "1.0.0"
    },
    "basePath": "/", \
    "schemes": [
        "http",
        "https"
    ]
}

swagger = Swagger(app, template=swagger_template)

if __name__ == '__main__':
    app.run(port=8080)
