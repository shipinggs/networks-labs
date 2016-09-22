from flask_wtf import Form
from wtforms import TextField, SubmitField

from wtforms import validators

class ContactForm(Form):
   name = TextField("Hi there, what is your name?",[validators.Required("Please enter your name.")])
   submit = SubmitField("Send")
