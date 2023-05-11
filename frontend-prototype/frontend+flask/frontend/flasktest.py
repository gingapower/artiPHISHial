from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/submit_data', methods=['POST'])
def submit_data():
    data = request.get_json()
    input_value = data['input']
    
    # Process the input value or perform any desired actions
    
    # Return the input value as a response
    return jsonify({'input': input_value})

if __name__ == '__main__':
    app.run(port=3000)
