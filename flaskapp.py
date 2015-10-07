'''
Created on Oct 7, 2015

@author: hugosenari
'''

from flask import Flask, render_template, Response, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/curl/')
def curl():
    url = request.args.get('url')
    if not url:
        return Response('{}', status=200, mimetype='application/json')

    env_key = request.args.get('key', '')
    key = os.env.get(env_key, '')

    url = url.format(key=key)
    my_request = requests.get(url)
    my_request.raise_for_status()
    json = my_request.text

    return Response(json, status=200, mimetype='application/json')


@app.route('/<post>')
def post(path):
    return render_template('{}/index.html'.format(post))

if __name__ == '__main__':
    app.run(debug=True)
