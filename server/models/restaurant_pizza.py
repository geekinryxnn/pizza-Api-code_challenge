from server import db
from sqlalchemy import CheckConstraint

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    
    pizza = db.relationship('Pizza', back_populates='restaurants')
    restaurant = db.relationship('Restaurant', back_populates='pizzas')
    
    def __repr__(self):
        return f'<RestaurantPizza ${self.price}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'pizza': self.pizza.to_dict(),
            'restaurant': self.restaurant.to_dict()
        }
    
    @classmethod
    def create(cls, **kwargs):
        try:
            restaurant_pizza = cls(**kwargs)
            db.session.add(restaurant_pizza)
            db.session.commit()
            return restaurant_pizza
        except Exception as e:
            db.session.rollback()
            raise ValueError(str(e))