import json
from flask import Flask, jsonify, request, Blueprint

payment_routes = Blueprint('payment_routes', __name__)

with open('db.json', 'r') as file:
    data = json.load(file)
    payments = data['payments']

#obtener todos los elementos
@payment_routes.route('/api/v1/payments', methods=['GET'])
def api_allpayments():
    return jsonify(payments)

#CREATE
@payment_routes.route('/api/v1/payments', methods=['POST'])
def create_payment():

    payment_data=request.get_json()

    payment_id= 1
    while any(payment['id'] == payment_id for payment in payments):
        payment_id += 1

    payment = {
        'id': payment_id,
        'date': payment_data['date'],
        'qr_img': payment_data['qr_img'],
        'attendee_id': payment_data['attendee_id'],
        'organizer_id': payment_data['organizer_id']
    }

    payments.append(payment)


    with open('db.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return jsonify(payment), 201

#READ
@payment_routes.route('/api/v1/payments/<int:id>', methods=['GET'])
def payment_id(id):

    for payment in payments:
        if payment['id'] == id:
            return jsonify(payment)
    return "Error: no se encontró el pago", 404

#UPDATE
@payment_routes.route('/api/v1/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    for payment in payments:
        if payment['id'] == id:
            updated_data = request.get_json()
            
            payment['date'] = updated_data['date']
            payment['qr_img'] = updated_data['qr_img']
            payment['attendee_id'] = updated_data['attendee_id']
            payment['organizer_id'] = updated_data['organizer_id']
            
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4)
            
            return "Pago actualizado correctamente"
    
    return "Error: no se encontró el pago", 404

#DELETE
@payment_routes.route('/api/v1/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    for payment in payments:
        if payment['id'] == id:
            payments.remove(payment)
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "Pago eliminado correctamente"
    return "Error: no se encontró el pago", 404
