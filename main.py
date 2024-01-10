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
    mortgage = db.Column(db.Integer)
    building_cost = db.Column(db.Integer)
    colour = db.Column(db.String(255))
    owner = db.Column(db.String(255))
    num_houses = db.Column(db.Integer)
    num_hotel = db.Column(db.Integer)

class Raildroad(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    mortgage = db.Column(db.Integer)
    owner = db.Column(db.String(255))

class Utility(db.Model):
    board_pos = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    mortgage = db.Column(db.Integer)
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

def create_property(board_pos, name, cost, base_rent, rent_one_house, rent_two_house, rent_three_house, rent_four_house, rent_hotel, mortgage, building_cost, colour, owner, num_houses, num_hotel):
	property = Property(board_pos=board_pos, name=name, cost=cost, base_rent=base_rent, rent_one_house=rent_one_house, rent_two_house=rent_two_house, rent_three_house=rent_three_house, rent_four_house=rent_four_house, rent_hotel=rent_hotel, mortgage=mortgage, building_cost=building_cost, colour=colour, owner=owner, num_houses=num_houses, num_hotel=num_hotel)
	db.session.add(property)
	db.session.commit()
	return property

def create_railroad(board_pos, name, cost, mortgage, owner):
	railroad = Raildroad(board_pos=board_pos, name=name, cost=cost, mortgage=mortgage, owner=owner)
	db.session.add(railroad)
	db.session.commit()
	return railroad

def create_utility(board_pos, name, cost, mortgage, owner):
	utility = Utility(board_pos=board_pos, name=name, cost=cost, mortgage=mortgage, owner=owner)
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
	
    property_data = properties()
    for board_pos, name, cost, base_rent, rent_one_house, rent_two_house, rent_three_house, rent_four_house, rent_hotel, mortgage, building_cost, colour, owner, num_houses, num_hotel in property_data:
          create_property(board_pos, name, cost, base_rent, rent_one_house, rent_two_house, rent_three_house, rent_four_house, rent_hotel, mortgage, building_cost, colour, owner, num_houses, num_hotel)

    railroad_data = railroads()
    for board_pos, name, cost, mortgage, owner in railroad_data:
          create_railroad(board_pos, name, cost, mortgage, owner)
    
    utility_data = utilities()
    for board_pos, name, cost, mortgage, owner in utility_data:
          create_utility(board_pos, name, cost, mortgage, owner)

    card_data = cards()
    for board_pos, name in card_data:
          create_card(board_pos, name)
    
    tax_data = tax()
    for board_pos, name, cost in tax_data:
          create_tax(board_pos, name, cost)
    
    extra_data = extra()
    for board_pos, name in extra_data:
          create_extra(board_pos, name) 






app.run(host='0.0.0.0', port=99, debug=True)