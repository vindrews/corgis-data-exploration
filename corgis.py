from flask import Flask, url_for, render_template, request
import json

app = Flask(__name__) 

@app.route("/page1.html")
def render_main():
    return render_template('page1.html')

@app.route("/response.html")
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
    return render_template('response.html', game = game)
if __name__=="__main__":
    app.run(debug=False)