from flask import Flask, render_template, request, redirect
from breaklist import breaklist
from datetime import date
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, func
from os import getenv
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField, DateField
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secretkey')

#getenv('db_uri')

db = SQLAlchemy(app)


class Match(db.Model):
    matchno= db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    Pl1 = db.Column(db.String(15))
    Pl2 = db.Column(db.String(15))
    Pl3 = db.Column(db.String(15))
    Pl4 = db.Column(db.String(15))
    Pl5 = db.Column(db.String(15))
    Pl6 = db.Column(db.String(15))
    Pl7 = db.Column(db.String(15))
    Pl8 = db.Column(db.String(15))
    Pl9 = db.Column(db.String(15))
    Pl10 = db.Column(db.String(15))


#db.drop_all()
db.create_all()

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

@app.route("/")
def home():
    matches = Match.query.all()
    return render_template("WholetableS.html", records=matches)

@app.route("/addgame")
def addgame():
    form = AddMatch()
    return render_template("AddGame.html", form=form)

@app.route("/savegame", methods=["GET", "POST"])
def savegame():
    form = AddMatch()
    playerlist = breaklist(form.playertext.data)
    if request.method == 'POST':
        date=form.date.data
        Pl1=playerlist[0]
        Pl2=playerlist[1]
        Pl3=playerlist[2]
        Pl4=playerlist[3]
        Pl5=playerlist[4]
        Pl6=playerlist[5]
        Pl7=playerlist[6]
        Pl8=playerlist[7]
        Pl9=playerlist[8]
        Pl10=playerlist[9]
        newmatch = Match(date=date, Pl1=Pl1, Pl2=Pl2, Pl3=Pl3, Pl4=Pl4, Pl5=Pl5, Pl6=Pl6, Pl7=Pl7, Pl8=Pl8, Pl9=Pl9, Pl10=Pl10)
        db.session.add(newmatch)
        db.session.commit()
        return redirect("/")
    return render_template("AddGame.html", form=form)



@app.route("/filtergame",methods=["POST"])
def filtergame():
    data = Match.query.filter( (Match.Pl1==request.form["filtername"]) | (Match.Pl2==request.form["filtername"]) | (Match.Pl3==request.form["filtername"]) 
                            | (Match.Pl4==request.form["filtername"]) | (Match.Pl5==request.form["filtername"])  | (Match.Pl6==request.form["filtername"]) | (Match.Pl7==request.form["filtername"])  
                            | (Match.Pl8==request.form["filtername"]) | (Match.Pl9==request.form["filtername"])  | (Match.Pl10==request.form["filtername"])   ).order_by(Match.date).all()
    n= len(data)
    name = request.form["filtername"]
    prova=data[0].date
    prova2= data[-1].date

    return render_template("WholetableS.html",records=data, n=n, name = name, prova=prova, prova2=prova2)


#@app.route("/playerpage/<str:name>")
#def playerpage(name):
#	data = Player.query.filter_by(name=name).first()
#	return render_template("playerpage.html",record=data)

#playerpage still to be done


@app.route('/editgame/<int:matchno>', methods=['GET', 'POST'])
def editgame(matchno):
    matchupd = Match.query.filter_by(matchno=matchno).first()
    form = UpdateMatch(date=matchupd.date, Pl1=matchupd.Pl1, Pl2=matchupd.Pl2, Pl3=matchupd.Pl3, Pl4=matchupd.Pl4,
                        Pl5=matchupd.Pl5, Pl6=matchupd.Pl6, Pl7=matchupd.Pl7, Pl8=matchupd.Pl8, Pl9=matchupd.Pl9,
                        Pl10=matchupd.Pl10
                         )
    
    if request.method == 'POST':
        matchupd.date = form.date.data
        matchupd.Pl1 = form.Pl1.data
        matchupd.Pl2 = form.Pl2.data
        matchupd.Pl3 = form.Pl3.data
        matchupd.Pl4 = form.Pl4.data
        matchupd.Pl5 = form.Pl5.data
        matchupd.Pl6 = form.Pl6.data
        matchupd.Pl7 = form.Pl7.data
        matchupd.Pl8 = form.Pl8.data
        matchupd.Pl9 = form.Pl9.data
        matchupd.Pl10 = form.Pl10.data
        db.session.commit()
        return redirect("/")
    return render_template('EditGame.html', form=form, record=matchupd)




@app.route("/deletegame/<int:matchno>")
def deletegame(matchno):
    matchdel = Match.query.filter_by(matchno=matchno).first()
    db.session.delete(matchdel)
    db.session.commit()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')