from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired
from climb.models import Record

class Add_record(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    grade = StringField('Grade', validators=[DataRequired()])
    sector = StringField('Sector', validators=[])
    location = StringField('Location', validators=[DataRequired()])
    date = DateField('Date of climb', validators=[])
    submit = SubmitField('Add')