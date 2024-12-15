from flask import Blueprint, jsonify, request

import service.config as config
from service.factory import ModelFactory
from service.validators import validate_input

api = Blueprint("api", __name__)

try:
    # Initialize model factory
    model_factory = ModelFactory(config.Config.MODEL_PATH)
    nlp = model_factory.load_model()
except FileNotFoundError as e:
    print(e)
    nlp = None


@api.route("/redact", methods=["POST"])
def redact_text():
    """
    API endpoint to redact PII entities from text.
    """
    # Check if the model was successfully loaded
    if nlp is None:
        return jsonify({"error": "Model not available. Please train the model first."}), 500

    text, error = validate_input()
    if error:
        return jsonify(error), 400

    try:
        redacted_text = model_factory.predict(text)
        return jsonify({"redacted_text": redacted_text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
