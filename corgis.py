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
        playercount = int(request.args['playercount'])
        year = request.args['year']
        rating = 0
        output = ""
        for x in data:
            if x['Features']['Max Players'] == playercount and str(x['Release']['Year']) == year and x['Metrics']['Review Score'] > rating:
                rating = x['Metrics']['Review Score']
                year = x['Release']['Year']
                playercount = x['Features']['Max Players']
                output = Markup("<p>Your perfect game would be " + x['Title'] + "! It has a review score of " + str(x['Metrics']['Review Score']) + " out of 100. It was released by " + x['Metadata']['Publishers'] + " in " + str(x['Release']['Year']) + ". Have fun playing!</p>")
        return render_template('page1.html', output = output)
    else:
        return render_template('page1.html')
    
#@app.route("/page2")
#def render_page2():
    #return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=False)