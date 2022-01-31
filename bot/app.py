"""The web gui to show information on the data."""
import os

from flask import Flask, render_template

from handler_functions.database_connector.select_db import get_customers
from web import config


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def home():
    data = get_customers()
    return render_template('home.html', **config.CONTEXT, customers=data)


if __name__ == "__main__":
    app.run(debug=True)
