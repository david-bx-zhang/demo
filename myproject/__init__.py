import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

# Often people will also separate these into a separate config.py file 
app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

# NOTE! These imports need to come after you've defined db, otherwise you will
# get errors in your models.py files.
## Grab the blueprints from the other views.py files for each "app"
from myproject.supply.views import supply_blueprint
from myproject.supplier.views import supplier_blueprint
from myproject.venue.views import venue_blueprint
from myproject.client.views import client_blueprint
from myproject.event.views import event_blueprint
from myproject.usedsupply.views import usedsupply_blueprint


app.register_blueprint(supply_blueprint,url_prefix='/supply')
app.register_blueprint(supplier_blueprint,url_prefix='/supplier')
app.register_blueprint(venue_blueprint,url_prefix='/venue')
app.register_blueprint(client_blueprint,url_prefix='/client')
app.register_blueprint(event_blueprint,url_prefix='/event')
app.register_blueprint(usedsupply_blueprint,url_prefix='/usedsupply')
