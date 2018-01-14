#Code Written by @Cosm00_
#Stay Based Youngins....

from flask import Flask, render_template, request
from threading import Thread
from sys import argv
import logging, time, sys

logging.getLogger('werkzeug').setLevel(logging.ERROR)

tokens = {'tokens':[]}

app = Flask(__name__)

def tokenremoval(token):
    tokens['tokens'].append(token)
    time.sleep(110)
    tokens['tokens'].remove(token)

@app.route('/json', methods=['GET'])
def json():
    content = tokens
    return(render_template('json.html', content = content))

@app.route('/solve', methods=['GET', 'POST'])
def solve():
    if request.method == "POST":
            token = request.form.get('g-recaptcha-response', '')
            Thread(target = tokenremoval, args = [token]).start()
    return(render_template('index.html', sitekey = sitekey))

@app.route('/sitekey', methods=['GET'])
def sitekey():
    return(render_template(sitekey))

if __name__ == '__main__':
    try:
        sitekey = argv[1]
    except IndexError:
        print('Error')
    Thread(target = app.run).start()
