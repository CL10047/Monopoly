from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import time
from sqlalchemy import exc, func, desc, asc
from board import properties, railroads, utilities, cards, tax, extra

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Monopoly'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Monopoly.db'
db = SQLAlchemy(app)

class Property(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    base_rent = db.Column(db.Integer)
    rent_one_house = db.Column(db.Integer)
    rent_two_house = db.Column(db.Integer)
    rent_three_house = db.Column(db.Integer)
    rent_four_house = db.Column(db.Integer)
    rent_hotel = db.Column(db.Integer)
    building_cost = db.Column(db.Integer)
    colour = db.Column(db.String(255))
    owner = db.Column(db.String(255))
    num_houses = db.Column(db.Integer)
    num_hotel = db.Column(db.Integer)

class Raildroad(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    owner = db.Column(db.String(255))

class Utility(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    owner = db.Column(db.String(255))

class Card(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Tax(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)

class Extra(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

def create_property(board_pos, name, cost, base_rent, rent_one_house, rent_two_house, rent_three_house, rent_four_house, rent_hotel, building_cost, colour, owner, num_houses, num_hotel):
	property = Property(board_pos=board_pos, name=name, cost=cost, base_rent=base_rent, rent_one_house=rent_one_house, rent_two_house=rent_two_house, rent_three_house=rent_three_house, rent_four_house=rent_four_house, rent_hotel=rent_hotel, building_cost=building_cost, colour=colour, owner=owner, num_houses=num_houses, num_hotel=num_hotel)
	db.session.add(property)
	db.session.commit()
	return property

def create_railroad(board_pos, name, cost, owner):
	railroad = Raildroad(board_pos=board_pos, name=name, cost=cost, owner=owner)
	db.session.add(railroad)
	db.session.commit()
	return railroad

def create_utility(board_pos, name, cost, owner):
	utility = Utility(board_pos=board_pos, name=name, cost=cost, owner=owner)
	db.session.add(utility)
	db.session.commit()
	return utility

def create_card(board_pos, name):
	card = Card(board_pos=board_pos, name=name)
	db.session.add(card)
	db.session.commit()
	return card

def create_tax(board_pos, name, cost):
	tax = Tax(board_pos=board_pos, name=name, cost=cost)
	db.session.add(tax)
	db.session.commit()
	return tax

def create_extra(board_pos, name):
	extra = Extra(board_pos=board_pos, name=name)
	db.session.add(extra)
	db.session.commit()
	return extra

with app.app_context():
    db.create_all()

    num_records = Property.query.count()
    if num_records == 0:
        property_data = properties()
        for el in property_data:
            create_property(el[0], el[1], el[2], el[3], el[4], el[5], el[6], el[7], el[8], el[9], el[10], el[11], el[12], el[13])
    
    num_records = Raildroad.query.count()
    if num_records == 0:
        railroad_data = railroads()
        for el in railroad_data:
            create_railroad(el[0], el[1], el[2], el[3])
    
    num_records = Utility.query.count()
    if num_records == 0:
        utility_data = utilities()
        for el in utility_data:
            create_utility(el[0], el[1], el[2], el[3])

    num_records = Card.query.count()
    if num_records == 0:
        card_data = cards()
        for el in card_data:
            create_card(el[0], el[1])
    
    num_records = Tax.query.count()
    if num_records == 0:
        tax_data = tax()
        for el in tax_data:
            create_tax(el[0], el[1], el[2])

    num_records = Extra.query.count()
    if num_records == 0:
        extra_data = extra()
        for el in extra_data:
            create_extra(el[0], el[1]) 

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/api/getPlayers', methods=['POST'])
def getPlayers():
    if (request.method == 'POST'):        
        numPlayers = request.form['playerCount']
        numBots = request.form['botCount']
        if (numPlayers == '' or numBots == ''):
            flash("Fill in the values", "error")
            return redirect(url_for('home'))
        elif (int(numPlayers) + int(numBots) > 6):
            flash("Max 6 total players", "error")
            return redirect(url_for('home'))
        else:
            return render_template('game.html')
    else:
         return redirect(url_for('home'))


app.run(host='0.0.0.0', port=99, debug=True)