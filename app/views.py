# views.py

from flask import render_template
from flask import request
from app import app

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import your module
import jeopardy

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")
