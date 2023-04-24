from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_data', methods=['POST'])
def submit_data():
    #email = request.form['login']
    #name = request.form['password']
    identifier = request.form['identifier']
    
    with open('user_data.txt', 'a') as file:
        #file.write(f'Name: {name}\n')
        #file.write(f'Email: {email}\n')
        file.write(f'Email: {identifier}\n')
    
    response_data = {
        'message': f'Daten gespeichert: Name: {identifier}'#, Email: {email}'
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
