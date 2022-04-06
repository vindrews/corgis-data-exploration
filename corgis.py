from flask import Flask, url_for, render_template, request
import json

app = Flask(__name__) 

@app.route("/")
def render_home():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
    return render_template('page1.html')

@app.route("/response")
def render_response():
    with open ('video_games.json') as ratings_data:
        data = json.load(ratings_data)
    playercount = request.args['playercount']
    handheld = request.args['handheld']
    rating = 0
    game = ['Title']
    for x in data:
        if x['Max Players'] == playercount and x['Handheld?'] == handheld and s['Review Score'] > rating:
            rating = s['Review Score']
            handheld = s['handheld']
            playercount = s['playercount']
    return render_template('response.html', game = game)
if __name__=="__main__":
    app.run(debug=False)