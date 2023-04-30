import datetime # import datetime module
from flask import Flask, render_template, request, cli # import Flask and render_template modules
import sys # import sys module for calling a source file above the current directory
import main as mn # import main module from parent directory
import csv # import csv module for csv file handling

# hide development server banner in terminal
cli.show_server_banner = lambda *_: None
# add parent directory to path
sys.path.append('../Even8') 
# path for csv file
sys.path.append('../..')

# create Flask app with name webserver.py
app = Flask(__name__)

# create route for index page
@app.route('/') 

 # define index function
def index():
    # open csv file
    with open("output.csv") as file:
        # get header
        reader = csv.reader(file)
        # get rows
        header = next(reader)
        # render index.html template and pass required variables
        return render_template('index.html', utc_dt=datetime.datetime.utcnow(), type="Seed", result=mn.main(), header=header, rows=reader) # render index.html template

# create route for encrypt page
@app.route('/encrypt' , methods=['POST']) 

# define encrypt function to encrypt password
def encrypt():
    # get content from form
    password = request.form['password']
    # encrypt password using main module
    encrypted_password = mn.small_password_encrypt(password)
    
    # open csv file
    with open("output.csv") as file:
        # get header
        reader = csv.reader(file)
        # get rows
        header = next(reader)
        # render index.html template with encrypted password as the result
        return render_template('index.html', utc_dt=datetime.datetime.utcnow(), type="Password", result=encrypted_password, header=header, rows=reader) # render index.html template

# method to run webserver
def host(): 
    # host webserver on all interfaces
    app.run(host='127.0.0.1')