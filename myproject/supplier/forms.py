from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name:')
    type = StringField('Type:')
    unit_price = StringField('Unit price:')
    contact = StringField('Contact:')
    supply_id = StringField('Supply_id:')
    submit = SubmitField('Add Supplier')

class UpdateForm(FlaskForm):
    id = StringField('Id')
    name = StringField('Name:')
    type = StringField('Type:')
    unit_price = StringField('Unit price:')
    contact = StringField('Contact:')
    supply_id = StringField('Supply_id:')
    submit = SubmitField('Update Supplier')

class QueryForm(FlaskForm):
    id = StringField('Id')
    name = StringField('Name:')
    type = StringField('Type:')
    unit_price = StringField('Unit price:')
    contact = StringField('Contact:')
    supply_id = StringField('Supply_id:')
    submit = SubmitField('Query Supplier')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Supplier to Remove:')
    submit = SubmitField('Remove Supplier')
