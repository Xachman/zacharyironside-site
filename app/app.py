from flask import Flask, render_template, request, abort, send_from_directory
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint
from src import Nav
from os import environ
app = Flask(__name__)
import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)

def log(input):
    pprint(vars(input), sys.stderr)

def link(linkpath):
    return  '<a href="'+linkpath+'"' 

@app.route('/admin')
@app.route('/admin/<path:path>')
def admin(path=''): 
    return "admin"


@app.route('/')
@app.route('/<path:path>')
def main(path=''):
    file = Path('./static/public/'+path)
    if file.is_file():
        return send_from_directory(directory='./static/public', filename=file.name)
    file = Path('./templates/content/'+path+'.html')
    nav = Nav.Nav(path)
    bodyclass = path.replace("/", "-")
    now = datetime.utcnow()
    if path == '':
        return render_template('layout.html', content_page='home', year=now.year, bodyclass='home', makeLink=nav.makeLink)
    elif file.is_file():
        return render_template('layout.html', content_page=path, year=now.year, bodyclass=bodyclass, makeLink=nav.makeLink)
    else:
        abort(404)


DEV = False
if environ.get('DEV') == 'true':
    DEV = True
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=DEV)