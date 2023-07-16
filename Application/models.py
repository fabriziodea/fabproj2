from Application import db

class Player(db.Model):
    name = db.Column(db.String(15), primary_key = True)
    caps = db.Column(db.Integer)
    first = db.Column(db.Date)
    last = db.Column(db.Date)
 #   Matches= db.relationship('Matches', backref='playerbr')


class Matches(db.Model):
    matchno= db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    Pl1 = db.Column(db.String(15))# foreign key removed
    Pl2 = db.Column(db.String(15))
    Pl3 = db.Column(db.String(15))
    Pl4 = db.Column(db.String(15))
    Pl5 = db.Column(db.String(15))
    Pl6 = db.Column(db.String(15))
    Pl7 = db.Column(db.String(15))
    Pl8 = db.Column(db.String(15))
    Pl9 = db.Column(db.String(15))
    Pl10 = db.Column(db.String(15))
