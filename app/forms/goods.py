from wtforms import StringField, IntegerField, Form
from wtforms.validators import Length, NumberRange, DataRequired

class SearchForm(Form):
    q = StringField(validators=[DataRequired(),Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=9999)], default=1)

class CategoryForm(Form):
    category = StringField(validators=[DataRequired(),Length(min=2, max=50)])
    page = IntegerField(validators=[NumberRange(min=1, max=9999)], default=1)