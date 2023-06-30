import json
from flask import Flask, jsonify, request, Blueprint

event_routes = Blueprint('event_routes', __name__)

with open('db.json', 'r') as file:
    data = json.load(file)
    events = data['events']

#obtener todos los elementos
@event_routes.route('/api/v1/events', methods=['GET'])
def api_allevents():
    return jsonify(events)

#CREATE
@event_routes.route('/api/v1/events', methods=['POST'])
def create_events():

    event_data=request.get_json()

    event_id= 1
    while any(event['id'] == event_id for event in events):
        event_id += 1

    event = {
        'id': event_id,
        'name': event_data['name'],
        'info': event_data['info'],
        'date': event_data['date'],
        'type': event_data['type'],
        'capacity': event_data['capacity']
    }

    events.append(event)


    with open('db.json', 'w') as file:
        json.dump(data, file, indent=3)
    
    return jsonify(event), 201

#READ
@event_routes.route('/api/v1/events/<int:id>', methods=['GET'])
def event_id(id):

    for event in events:
        if event['id'] == id:
            return jsonify(event)
    return "Error: no se encontró el evento", 404

#UPDATE
@event_routes.route('/api/v1/events/<int:id>', methods=['PUT'])
def update_event(id):
    for event in events:
        if event['id'] == id:
            updated_data = request.get_json()
            event['name']: updated_data['name']
            event['info'] = updated_data['info']
            event['date'] = updated_data['date']
            event['type'] = updated_data['type']
            event['capacity'] = updated_data['capacity']
            
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=3)
            
            return "Evento actualizado correctamente"
    
    return "Error: no se encontró el evento", 404

#DELETE
@event_routes.route('/api/v1/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    for event in events:
        if event['id'] == id:
            events.remove(event)
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "Evento eliminado correctamente"
    return "Error: no se encontró el evento", 404
