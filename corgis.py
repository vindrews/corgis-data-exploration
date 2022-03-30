from flask import Flask, url_for, render_template, request
import random

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    one = request.args['one']
    two = request.args['two']
    three = request.args['three']
    four = request.args['four']
    yes = request.args['yes']
    no = request.args['no']
    nopref = request.args['nopref']
    