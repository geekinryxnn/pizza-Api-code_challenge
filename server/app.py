from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from server.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
app.register_blueprint(pizza_bp, url_prefix='/pizzas')
app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Pizza Restaurant API"})

if __name__ == '__main__':
    app.run(debug=True)