from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, DateField

class AddMatch(FlaskForm):
    date = DateField("date")
    playertext = StringField("playertext")
    submit = SubmitField('Add Match')


class UpdateMatch(FlaskForm):
    date = DateField("date")
    Pl1 = StringField("Pl1")
    Pl2 = StringField("Pl2")
    Pl3 = StringField("Pl3")
    Pl4 = StringField("Pl4")
    Pl5 = StringField("Pl5")
    Pl6 = StringField("Pl6")
    Pl7 = StringField("Pl7")
    Pl8 = StringField("Pl8")
    Pl9 = StringField("Pl9")
    Pl10 = StringField("Pl10")
    submit = SubmitField('Update Match')