import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.repositories.peep_repository import PeepRepository


app = Flask(__name__)
app.jinja_env.autoescape = True

@app.route("/home", methods=['GET'])
def get_peeps():
    connection = get_flask_database_connection(app)
    repo = PeepRepository(connection)

    peeps = repo.all()
    return render_template('index.html', peeps=peeps) # 


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


