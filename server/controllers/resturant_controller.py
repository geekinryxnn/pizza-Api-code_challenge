from flask import Blueprint, jsonify, abort
from server.config import db
from server.models.restaurant import Restaurant

bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants])

@bp.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        abort(404, description='Restaurant not found')
    return jsonify(restaurant.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        abort(404, description='Restaurant not found')
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204