from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6aebb273b8ed6f620238a539c962f934'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from src.models import Cart, Product, CartItem, Order
from src.routes import cart, product, cart_item, order, database

cart.add_routes(app)
product.add_routes(app)
cart_item.add_routes(app)
order.add_routes(app)
database.add_routes(app)
