import datetime
from Application import app, db
from Application.models import Player, Matches
from sqlalchemy import extract


x = datetime.datetime(2018, 6, 1)

print(x)
print("ciao")


match = Matches.query.first()
print(match.date.year)

#matchdel = Matches.query.filter(matchno=matchno).first()

#data = Matches.query.filter(Matches.date.year=='2021').all()
data = Matches.query.filter(extract('year', Matches.date) == 2021).subquery()
porco = data.query.filter_by(Pl1==Herve).first()
porco2= Matches.query.filter()

for m in data:
    print(m.date)

print(porco)


