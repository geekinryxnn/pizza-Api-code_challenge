from flask import Blueprint, jsonify
from server.config import db
from server.models.pizza import Pizza

bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')

@bp.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([p.to_dict() for p in pizzas])