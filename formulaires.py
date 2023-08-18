from wtforms import Form, StringField, TextAreaField, validators, SubmitField, PasswordField, BooleanField, SelectField, IntegerField, FloatField, DateField
from wtforms.validators import DataRequired 


class UserForm(Form):
    name = StringField('name', [validators.Length(min=1, max=50)])
    username = StringField('username', [validators.Length(min=4, max=25)])
    email = StringField('email', [validators.Length(min=6, max=50)])
    phone = StringField('phone', [validators.Length(min=7, max=14)])
    website = StringField('website', [validators.Length(min=4, max=50)])
    street = StringField('street', [validators.Length(min=4, max=50)])
    suite = StringField('suite', [validators.Length(min=4, max=50)])
    city = StringField('city', [validators.Length(min=4, max=50)])
    zipcode = StringField('zipcode', [validators.Length(min=4, max=50)])
    lng = StringField('lng', [validators.Length(min=4, max=50)])
    lat = StringField('lat', [validators.Length(min=4, max=50)])
    name_company=StringField('name_company')
    catchPrase=StringField('catchPrase')
    bs=StringField('bs')