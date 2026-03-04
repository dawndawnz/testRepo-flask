from flask import Flask
app=Flask(__first__)
@app.route("/")
def hello_world():
    return "Hello World!"

