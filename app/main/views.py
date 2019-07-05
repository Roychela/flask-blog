from flask import render_template
from . import main

@main.route('/')
def index():
    posts = [{'title':'abc'}, {'content':'lmn'}, {'id':'aqw'}]
    return render_template('index.html', posts=posts)