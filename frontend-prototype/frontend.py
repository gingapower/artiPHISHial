from flask import Flask, render_template, request
from another_python_file import execute_function
import scraper

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('frontend-template', 'index.html')

def submit():
    input_content = request.form['myInput']
    scraper.

if __name__ == '__main__':
    app.run()