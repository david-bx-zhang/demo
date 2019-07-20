from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name:')
    client_id = StringField('Client id')
    type = StringField('Type')
    date = StringField('Date')
    num_of_invitees = StringField('Num_of_invitees')
    budget = StringField('Budget:')
    venue_id = StringField('Venue_id:')
    submit = SubmitField('Add Event')

class UpdateForm(FlaskForm):
    id = StringField('Id')
    name = StringField('Name:')
    client_id = StringField('Client id')
    type = StringField('Type')
    date = StringField('Date')
    num_of_invitees = StringField('Num_of_invitees')
    budget = StringField('Budget:')
    venue_id = StringField('Venue_id:')
    submit = SubmitField('Update Event')

class QueryForm(FlaskForm):
    id = StringField('Id')
    submit = SubmitField('Query Event')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Event to Remove:')
    submit = SubmitField('Remove Event')
