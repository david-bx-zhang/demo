from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name:')
    type = StringField('Type:')
    location = StringField('Location:')
    price = StringField('Price:')
    contact = StringField('Contact:')
    submit = SubmitField('Add Venue')


class UpdateForm(FlaskForm):
    id = StringField('Id')
    name = StringField('Name:')
    type = StringField('Type:')
    location = StringField('Location:')
    price = StringField('Price:')
    contact = StringField('Contact:')
    submit = SubmitField('Update Venue')

class QueryForm(FlaskForm):
    id = StringField('Id')
    name = StringField('Name:')
    type = StringField('Type:')
    location = StringField('Location:')
    price = StringField('Price:')
    contact = StringField('Contact:')
    submit = SubmitField('Query Venue')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Venue to Remove:')
    submit = SubmitField('Remove Venue')
