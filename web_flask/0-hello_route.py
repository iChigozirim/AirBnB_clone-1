#!/usr/bin/python3
"""Starts Flask web application."""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Displys 'Hello HBNB!'"""
    return "<h1>Hello HBNB!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
