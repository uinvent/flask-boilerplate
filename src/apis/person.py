"""
Handles Person related APIs
"""
from flask import request
from infra import app
from src.apis.utils import json_response, json_error_response
from src.models import db
from src.models.person import Person
import logging

ROUTE_PREFIX = '/person/'


@app.route(ROUTE_PREFIX, methods=['GET'])
@app.route(ROUTE_PREFIX + '/<person_id>', methods=['GET'])
def get(person_id=None):
    """
    Get or Get All person entities
    :param person_id: [id] of the required person
    :return: Return all person entities or the person entity with the [id] matched
    """
    result = []
    if not person_id:
        persons = db.session.query(Person).order_by(Person.id).all()
        result = [person.serialize for person in persons]
    else:
        person = db.session.query(Person).get(person_id)
        if not person:
            return json_response('No Result Found')
        result = person.serialize
    return json_response(result)


@app.route(ROUTE_PREFIX + '/<person_id>/address/', methods=['GET'])
def get_person_address(person_id=None):
    """
    Get person and its address entities
    :param person_id: [id] of the person to found
    :return: person and its address details
    """
    result = []
    if not person_id:
        raise Exception('Person Id is missing in request.')
    person = db.session.query(Person).get(person_id)
    if not person:
        return json_response('No Result Found')
    result = person.serialize
    result['address'] = [address.serialize for address in person.addresses]

    return json_response(result)


@app.route(ROUTE_PREFIX, methods=['POST'])
def post():
    """
    Create a person entity on the basis of request.
    :return: New created person entity
    """
    form_dict = request.get_json()
    try:
        new_person = Person()
        new_person.from_dict(form_dict)
        db.session.add(new_person)
        db.session.commit()
        return json_response(new_person.serialize)
    except Exception as e:
        logging.exception(e)
        return json_error_response(e)


@app.route(ROUTE_PREFIX + '<person_id>', methods=['DELETE'])
def delete(person_id):
    """
    Delete the person entity with [id] matched
    :param person_id:
    :return: Success response message
    """
    try:
        if not person_id:
            return json_response('No Id provided')
        person = db.session.query(Person).get(person_id)
        if not person:
            return json_response('Record not found')
        db.session.delete(person)
        db.session.commit()
        return json_response('Successfully Deleted')
    except Exception as e:
        logging.exception(e)
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
        person = db.session.query(Person).get(person_id)
        person.from_dict(form_dict)
        db.session.add(person)
        db.session.commit()
        return json_response(person.serialize)
    except Exception as e:
        logging.exception(e)
        return json_error_response(e)
