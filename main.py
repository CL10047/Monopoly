from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import time
from sqlalchemy import exc, func, desc, asc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Monopoly'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Monopoly.db'
db = SQLAlchemy(app)



app.run(host='0.0.0.0', port=99, debug=True)