"""
Utility methods for APIs
"""
import json
from flask import Response


def json_response(json_input, status=200):
    return Response(
        json.dumps(json_input, indent=4, sort_keys=True, default=str),
        status=status,
        mimetype="application/json")


def json_error_response(msg=None, status=500, stacktrace=None, payload=None):
    if not payload:
        payload = {'error': str(msg)}
        if stacktrace:
            payload['stacktrace'] = stacktrace
    return json_response(payload, status)
