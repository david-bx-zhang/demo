from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    name = StringField('Name:')
    bill_info = StringField('Bill info:')
    submit = SubmitField('Add Client')

class UpdateForm(FlaskForm):
    id = StringField('Id:')
    name = StringField('Name:')
    bill_info = StringField('Bill info:')
    submit = SubmitField('Update Client')


class QueryForm(FlaskForm):
    id = StringField('Id:')
    name = StringField('Name:')
    bill_info = StringField('Bill info:')
    submit = SubmitField('Query Client')



class DelForm(FlaskForm):

    id = IntegerField('Id Number of Client to Remove:')
    submit = SubmitField('Remove Client')
