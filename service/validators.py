from flask import jsonify, request


def validate_input():
    """
    Validate JSON input for the API.
    """
    data = request.get_json()
    if not data or "text" not in data:
        return {"error": "Missing 'text' in request body"}, 400
    return data["text"], None
