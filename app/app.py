from flask import Flask, render_template, request, abort
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint
app = Flask(__name__)


def log(input):
    pprint(vars(input), sys.stderr)


@app.route('/admin')
@app.route('/admin/<path:path>')
def admin(path=''): 
    return "admin"


@app.route('/')
@app.route('/<path:path>')
def main(path=''):
    file = Path('./templates/content/'+path+'.html')
    now = datetime.utcnow()
    if path == '':
        return render_template('layout.html', content_page='home', year=now.year)
    elif file.is_file():
        return render_template('layout.html', content_page=path, year=now.year)
    else:
        abort(404)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)