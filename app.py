import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.jinja_env.autoescape = True


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))