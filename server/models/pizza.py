from server import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    
    restaurants = db.relationship('RestaurantPizza', back_populates='pizza')
    
    def __repr__(self):
        return f'<Pizza {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }
    
    @classmethod
    def get_all_serialized(cls):
        pizzas = cls.query.all()
        return [pizza.to_dict() for pizza in pizzas]