import uuid
from flask_cors import CORS
from flask import Flask, request, jsonify

CONTACTS = [
    {
        'id': uuid.uuid4().hex,
        'first_name': 'John',
        'last_name': 'Barrymore',
        'mobile_number': '+380672363493',
    },
    {
        'id': uuid.uuid4().hex,
        'first_name': 'Bill',
        'last_name': 'Dalton',
        'mobile_number': '+380993937204',
    },
    {
        'id': uuid.uuid4().hex,
        'first_name': 'Sam',
        'last_name': 'Rutherford',
        'mobile_number': '+380680391227',
    },
    {
        'id': uuid.uuid4().hex,
        'first_name': 'Peter',
        'last_name': 'Bohr',
        'mobile_number': '+380962379305',
    },
    {
        'id': uuid.uuid4().hex,
        'first_name': 'Albert',
        'last_name': 'Curie',
        'mobile_number': '+380972951737',
    },
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

@app.route('/contacts', methods=['GET', 'POST'])
def all_contacts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        CONTACTS.append({
            'id': uuid.uuid4().hex,
            'first_name': post_data.get('first_name'),
            'last_name': post_data.get('last_name'),
            'mobile_number': post_data.get('mobile_number')
        })
        response_object['message'] = 'Contact added!'
    else:
        response_object['contacts'] = CONTACTS
    return jsonify(response_object)

@app.route('/contacts/<contact_id>', methods=['PUT', 'DELETE'])
def single_contact(contact_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_contact(contact_id)
        CONTACTS.append({
            'id': uuid.uuid4().hex,
            'first_name': post_data.get('first_name'),
            'last_name': post_data.get('last_name'),
            'mobile_number': post_data.get('mobile_number')
        })
        response_object['message'] = 'Contact updated!'
    if request.method == 'DELETE':
        remove_contact(contact_id)
        response_object['message'] = 'Contact removed!'
    return jsonify(response_object)

def remove_contact(contact_id):
    for contact in CONTACTS:
        if contact['id'] == contact_id:
            CONTACTS.remove(contact)
            return True
    return False

if __name__ == '__main__':
    app.run()