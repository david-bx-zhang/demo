from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name:')
    type = StringField('Type:')
    submit = SubmitField('Add Supply')

class UpdateForm(FlaskForm):
    id = StringField('id:')
    name = StringField('Name:')
    type = StringField('Type:')
    submit = SubmitField('Update Supply')

class QueryForm(FlaskForm):
    id = StringField('id:')
    name = StringField('Name:')
    type = StringField('Type:')
    submit = SubmitField('Query Supply')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Supply to Remove:')
    submit = SubmitField('Remove Supply')
