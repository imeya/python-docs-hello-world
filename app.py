from flask import Flask
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    print("hello, this is a test log from print() method...")
    logging.exception("exeption is from logging.exception() method...")
    logging.info("info is from logging.info() method...")
    return "Hello, World!"
