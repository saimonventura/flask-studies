from flask import Flask
from flask_restful import Api

from controllers.setup import Controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'FF57EF2682739384F4889BE3ABB3FD25'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


Controller(app, api)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
