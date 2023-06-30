import json
from flask import Flask, jsonify, request, Blueprint

organizer_routes = Blueprint('organizer_routes', __name__)

with open('db.json', 'r') as file:
    data = json.load(file)
    organizers = data['organizers']

#obtener todos los elementos
@organizer_routes.route('/api/v1/organizers', methods=['GET'])
def api_allorganizers():
    return jsonify(organizers)

#CREATE
@organizer_routes.route('/api/v1/organizers', methods=['POST'])
def create_organizers():

    organizer_data=request.get_json()

    organizer_id= 1
    while any(organizer['id'] == organizer_id for organizer in organizers):
        organizer_id += 1

    organizer = {
        'id': organizer_id,
        'name': organizer_data['name'],
        'user_name': organizer_data['user_name'],
        'email': organizer_data['email'],
        'password': organizer_data['password']
    }

    organizers.append(organizer)


    with open('db.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return jsonify(organizer), 201

#READ
@organizer_routes.route('/api/v1/organizers/<int:id>', methods=['GET'])
def organizer_id(id):

    for organizer in organizers:
        if organizer['id'] == id:
            return jsonify(organizer)
    return "Error: no se encontró al organizador", 404

#UPDATE
@organizer_routes.route('/api/v1/organizers/<int:id>', methods=['PUT'])
def update_organizer(id):
    for organizer in organizers:
        if organizer['id'] == id:
            updated_data = request.get_json()
            organizer['name']: updated_data['name']
            organizer['user_name'] = updated_data['user_name']
            organizer['email'] = updated_data['email']
            organizer['password'] = updated_data['password']
            
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4)
            
            return "Organizador actualizado correctamente"
    
    return "Error: no se encontró al organizador", 404

#DELETE
@organizer_routes.route('/api/v1/organizers/<int:id>', methods=['DELETE'])
def delete_organizer(id):
    for organizer in organizers:
        if organizer['id'] == id:
            organizers.remove(organizer)
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "organizador eliminado correctamente"
    return "Error: no se encontró al organizador", 404
