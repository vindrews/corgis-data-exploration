from flask import Flask, url_for, render_template, request
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/page1.html")
def render_main():
    return render_template('page1.html')

@app.route("/response")
def render_response():
    playercount = request.args['playercount']
    handheld = request.args['handheld']
    

    if handheld == yes and playercount == 1:
        response = hello
    else:
        response = goodbye
    return render_template('response.html', response = response)

        
        
if __name__=="__main__":
    app.run(debug=False)