import os
import pickle
from werkzeug.exceptions import BadRequestKeyError
from flask import Flask, request, render_template, redirect
import sys

cwd = os.getcwd()

with open('data.pkl', 'rb') as f:
    variable_names = pickle.load(f)

with open(os.path.join(cwd, "url"), 'r') as f:
    url = f.read()

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_data', methods=['POST'])
def submit_data():
    # Create an empty dictionary to store the form data
    form_data = {}

    # Loop over the variable names and add the form data to the dictionary
    for var_name in variable_names:
        try:
            form_data[var_name] = request.form[var_name]
        except BadRequestKeyError as e:
            # Extract the KeyError value from the exception
            key_error_value = e.args[0]
            variable_names.remove(key_error_value)
            with open('data.pkl', 'wb') as f:
                pickle.dump(variable_names, f)
            return "Error has been detected. App restarted successfully! Please reload the page!"

    # Write the form data to a file
    with open('user_data.txt', 'a') as file:
        file.write(f'Form Data: {form_data}\n')

    response_data = {
        'message': f'Daten gespeichert: {form_data}'
    }

    return redirect(url)
    # return jsonify(response_data)


if __name__ == '__main__':
  app.run(port=4000,debug=True)
