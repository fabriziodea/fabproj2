from flask import Flask, render_template, request, redirect
from breaklist import breaklist
from datetime import date
import mysql.connector

db=mysql.connector.connect(     host="localhost",
                                user="root",
                                password="rootroot",
                                database="frizzo"
)
cursor =db.cursor()
application=Flask(__name__)

@application.route("/")
def homepage():
    cursor.execute("Select * from calcetto")
    data=cursor.fetchall()
    return render_template("wholetable.html", records=data)

@application.route("/addgame")
def add():
    return render_template("addgame.html")


@application.route("/savegame", methods=["POST"])
def savegame():
    d=request.form["day"]
    rawtext=request.form["playertext"]
    plist= breaklist(rawtext)


    sqlquery="insert into calcetto values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}')".format(d, plist[0], plist[1], plist[2], plist[3], plist[4], plist[5],plist[6], plist[7], plist[8], plist[9])
    cursor.execute(sqlquery)
    db.commit()
    return redirect("/")

@application.route("/deletegame/<date>")
def delete(date):
    cursor.execute("Delete from calcetto where day='{0}'".format(date))
    db.commit()
    return redirect("/")


application.run(debug=True)