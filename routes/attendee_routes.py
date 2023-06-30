import json
from flask import Flask, jsonify, request, Blueprint

attendee_routes = Blueprint('attendee_routes', __name__)

with open('db.json', 'r') as file:
    data = json.load(file)
    attendees = data['attendees']

#obtener todos los elementos
@attendee_routes.route('/api/v1/attendees', methods=['GET'])
def api_allattendees():
    return jsonify(attendees)

#CREATE
@attendee_routes.route('/api/v1/attendees', methods=['POST'])
def create_attendees():

    attendee_data=request.get_json()

    attendee_id= 1
    while any(attendee['id'] == attendee_id for attendee in attendees):
        attendee_id += 1

    attendee = {
        'id': attendee_id,
        'name': attendee_data['name'],
        'user_name': attendee_data['user_name'],
        'email': attendee_data['email'],
        'password': attendee_data['password']
    }

    attendees.append(attendee)


    with open('db.json', 'w') as file:
        json.dump(data, file, indent=3)
    
    return jsonify(attendee), 201

#READ
@attendee_routes.route('/api/v1/attendees/<int:id>', methods=['GET'])
def attendee_id(id):

    for attendee in attendees:
        if attendee['id'] == id:
            return jsonify(attendee)
    return "Error: no se encontró al asistente", 404

#UPDATE
@attendee_routes.route('/api/v1/attendees/<int:id>', methods=['PUT'])
def update_attendee(id):
    for attendee in attendees:
        if attendee['id'] == id:
            updated_data = request.get_json()
            attendee['name']: updated_data['name']
            attendee['user_name'] = updated_data['user_name']
            attendee['email'] = updated_data['email']
            attendee['password'] = updated_data['password']
            
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=3)
            
            return "Asistente actualizado correctamente"
    
    return "Error: no se encontró al asistente", 404

#DELETE
@attendee_routes.route('/api/v1/attendees/<int:id>', methods=['DELETE'])
def delete_attendee(id):
    for attendee in attendees:
        if attendee['id'] == id:
            attendees.remove(attendee)
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "Asistente eliminado correctamente"
    return "Error: no se encontró al asistente", 404
