"""
Handles Person APIs
Performs request and response serialization and deserialization respectively
For business logic implementation; it relies on service layer.
"""
from flask import request
from infra import app
from src.apis.utils import json_response, json_error_response
from src.models import PersonModel
from src.services.person import PersonService

ROUTE_PREFIX = '/person/'
person_service = PersonService()


@app.route(ROUTE_PREFIX, methods=['GET'])
@app.route(ROUTE_PREFIX + '/<person_id>', methods=['GET'])
def get(person_id=None):
    """
    Get or Get All person entities
    :param person_id: [id] of the required person
    :return: Return all person entities or the person entity with the [id] matched
    """
    try:
        if not person_id:
            persons = person_service.get_all()
            result = [person.serialize for person in persons]
        else:
            person = person_service.get(person_id)
            result = person.serialize
        return json_response(result)
    except Exception as e:
        return json_error_response(e)


@app.route(ROUTE_PREFIX + '/<person_id>/address/', methods=['GET'])
def get_person_address(person_id):
    """
    Get person and its address entities
    :param person_id: [id] of the person to found
    :return: person and its address details
    """
    try:
        person = person_service.get(person_id)
        result = person.serialize
        result['address'] = [address.serialize for address in person.addresses]
        return json_response(result)

    except Exception as e:
        return json_error_response(e)


@app.route(ROUTE_PREFIX, methods=['POST'])
def post():
    """
    Create a person entity on the basis of request.
    :return: New created person entity
    """
    form_dict = request.get_json()
    try:
        person = PersonModel()
        person.from_dict(form_dict)
        person = person_service.create(person)
        return json_response(person.serialize)
    except Exception as e:
        return json_error_response(e)


@app.route(ROUTE_PREFIX + '<person_id>', methods=['DELETE'])
def delete(person_id):
    """
    Delete the person entity with [id] matched
    :param person_id:
    :return: Success response message
    """
    try:
        person_service.delete(person_id)
        return json_response('Successfully Deleted')
    except Exception as e:
        return json_error_response(e)


@app.route(ROUTE_PREFIX + "<person_id>", methods=['PUT'])
def update(person_id):
    """
    Update the person entity on the basis of request object and [id] passed
    :param person_id: id of the person entity to be updated
    :return: updated person entity
    """
    form_dict = request.get_json()
    try:
        person = person_service.get(person_id)
        person.from_dict(form_dict)
        person = person_service.update(person)
        return json_response(person.serialize)
    except Exception as e:
        return json_error_response(e)
