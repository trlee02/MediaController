from flask import Flask
app = Flask(__name__)
@app.route("/")

def index():
    return "The Server is up and running"



app.run()