from flask import Flask, render_template, redirect, request, url_for
import requests

app = Flask(__name__)

@app.route('/')
def index(city=None):
    if(city == None):
        return render_template('index.html')
    else:
        # do actual stuff here
        return render_template('index.html', **locals())

@app.route('/', methods=['POST'])
def indexPost():
    city = request.form["citydropdown"]

    # So I think we can do the scripting part in the index() method after
    # a city is inputted
    return index(city)

if __name__ == "__main__":
	app.run(port="5000")
