from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Match
import datetime
import application.routes

#from application.forms import AddMatch, UpdateMatch



class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
                        )
        return app

    def setUp(self):
        db.create_all()
        sample = Match(date=datetime.date(2020, 5, 17), Pl1='Johna', Pl2='Johnb', Pl3='Johnc', Pl4='Johnd', Pl5='Johne', Pl6='Johnf',
                        Pl7='Johng',Pl8='Johnh',Pl9='Johni',Pl10='Johnj')
        db.session.add(sample)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_match_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Johna', response.data)

    def test_add_game(self):
        response = self.client.get(url_for('addgame'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add another game', response.data)

    def test_edit_game(self):
        response = self.client.get(url_for('editgame', matchno=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update game', response.data)

    def test_mostcaps(self):
        response = self.client.get(url_for('mostcaps'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Most Capped', response.data)

    def test_playerpage(self):
        response = self.client.get(url_for('playerpage', playername='Johne'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CAPS', response.data)

    def test_save_game(self):
        response = self.client.post(url_for('savegame'),
        data = dict( date=datetime.date(2021, 11, 21), playertext= 'Jima Jimb Jimc Jimd Jime Jimf Jimg Jimh Jimi Jimj'),
        follow_redirects = True
        )
        self.assertIn(b'Jimc', response.data)
    
    def test_filter_game(self):
        response = self.client.post(url_for('filtergame'),
        data = dict(filtername='Johnd'))
        self.assertIn(b'Johnd', response.data)

    def test_del_game(self):
        response = self.client.get(url_for('deletegame', matchno=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Monday Games', response.data)

    def test_update_game(self):
        response = self.client.post(
            url_for('editgame', matchno=1),
            data = dict(date=datetime.date(2019, 12, 31), Pl1='Jaya', Pl2='Jayb', Pl3='Jayc', Pl4='Jayd', Pl5='Jaye', Pl6='Jayf',
                        Pl7='Jayg',Pl8='Jayh',Pl9='Jayi',Pl10='Jayj'),
            follow_redirects = True
        )
        self.assertIn(b'Jayi', response.data)