import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.jinja_env.autoescape = True

@app.route("/home", methods=['GET'])
def get_peeps():
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


