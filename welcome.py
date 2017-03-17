from flask import Flask, render_template, request, send_from_directory

import sqlite3 as sql
import requests
app = Flask(__name__)
from datetime import datetime
import itertools
data=[]

@app.route('/',methods = ['POST', 'GET'])
def home():
	return render_template('home.html')

@app.route('/<path:path>', methods=['POST', 'GET'])
def static_proxy(path):
    return send_from_directory('static', path)
		
			
if __name__ == '__main__':
   app.run(debug = False)