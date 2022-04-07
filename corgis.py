from flask import Flask, url_for, render_template, request
import json
from markupsafe import Markup, escape

app = Flask(__name__) 

@app.route("/")
def render_home():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
    if "playercount" in request.args:
        with open ('video_games.json') as ratings_data:
            data = json.load(ratings_data)
        playercount = request.args['playercount']
        handheld = request.args['handheld']
        rating = 0
        game = ['Title']
        output = ""
        for x in data:
            if x['Features']['Max Players'] == playercount and x['Features']['Handheld?'] == handheld and s['Review Score'] > rating:
                rating = s['Metrics']['Review Score']
                handheld = s['Features']['handheld']
                playercount = s['Features']['playercount']
                output = Markup("<p>Your perfect game would be" + s['Title'] + "! It has a review score of" + s['Metrics']['Review Score'] + "out of 100. It was released by" + s['Metadata']['Publishers'] + ". Have fun playing!</p>")
        return render_template('page1.html', output = output)
    else:
        return render_template('page1.html')
if __name__=="__main__":
    app.run(debug=False)