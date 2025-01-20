# server.py
import argparse
import logging

from flask import Flask, request, jsonify
from service import InventoryService

app = Flask(__name__)
service = InventoryService()

@app.route('/define_stuff', methods=['POST'])
def define_stuff():
    data = request.json
    type = data.get('type')
    description = data.get('description')
    result = service.define_stuff(type, description)
    return jsonify({'message': result})

@app.route('/undefine', methods=['POST'])
def undefine():
    data = request.json
    type = data.get('type')
    result = service.undefine(type)
    return jsonify({'message': result})

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    quantity = data.get('quantity')
    type = data.get('type')
    result = service.add(quantity, type)
    return jsonify({'message': result})

@app.route('/remove', methods=['POST'])
def remove():
    data = request.json
    quantity = data.get('quantity')
    type = data.get('type')
    result = service.remove(quantity, type)
    return jsonify({'message': result})
    
@app.route('/get_count/<type>', methods=['GET'])
def get_count_route(type):
    count = service.get_count(type)
    return jsonify({'count': count})


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description="A simple Python program with configurable parameter.")
    parser.add_argument('arg1', nargs='?', default='localhost', help='Input argument (default: "default_value")')
    args = parser.parse_args()
    
    app.run(host=args.arg1, port=5000, debug=True)
