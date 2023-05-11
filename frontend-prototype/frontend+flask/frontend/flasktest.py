from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/submit_data', methods=['POST'])
def submit_data():
    data = request.json  # Assuming the request contains JSON data

    # Process the data
    # ...

    # Return a response
    print(data)
    response = {'message': 'Data received successfully'}
    return jsonify(response)

if __name__ == '__main__':
    app.run()