from flask import Blueprint, jsonify, request, abort
from server.config import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        # Validate foreign keys
        if not Restaurant.query.get(data['restaurant_id']):
            abort(400, description='Restaurant not found')
        if not Pizza.query.get(data['pizza_id']):
            abort(400, description='Pizza not found')
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    except ValueError as e:
        abort(400, description=str(e))