from flask import Flask, request, jsonify
import sys


app = Flask(__name__)


# Local in-memory storage
local_data = {}


@app.route('/put', methods=['PUT'])
def store_data():
body = request.get_json()


if not body or 'key' not in body or 'value' not in body:
return jsonify({'message': 'Invalid input'}), 400


k = body['key']
v = body['value']


local_data[k] = v
return jsonify({'message': 'Saved successfully'}), 200




@app.route('/get', methods=['GET'])
def fetch_data():
k = request.args.get('key')


if k not in local_data:
return jsonify({'message': 'Key does not exist'}), 404


return jsonify({'key': k, 'value': local_data[k]}), 200




if __name__ == '__main__':
port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
app.run(host='127.0.0.1', port=port)
