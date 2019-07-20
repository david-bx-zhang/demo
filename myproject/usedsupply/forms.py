from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    supply_id = StringField('Supply_id:')
    event_id = StringField('Event_id:')
    quantity = StringField('Quantity:')
    submit = SubmitField('Add used supply')

class UpdateForm(FlaskForm):
    id = StringField('id:')
    supply_id = StringField('Supply_id:')
    event_id = StringField('Event_id:')
    quantity = StringField('Quantity:')
    submit = SubmitField('Update used supply')


class DelForm(FlaskForm):
    id = StringField('id:')
    submit = SubmitField('Remove usedsupply')
