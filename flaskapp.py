'''
Created on Oct 7, 2015

@author: hugosenari
'''


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
