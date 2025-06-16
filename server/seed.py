from server.app import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    db.drop_all()
    db.create_all()
    
    # Seed Restaurants
    r1 = Restaurant(name="Dominion Pizza", address="123 Main St")
    r2 = Restaurant(name="Pizza Palace", address="456 Oak Ave")
    r3 = Restaurant(name="Kiki's Pizza", address="789 Pine Rd")
    
    # Seed Pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    
    db.session.add_all([r1, r2, r3, p1, p2])
    db.session.commit()
    
    # Seed RestaurantPizzas
    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)
    
    db.session.add_all([rp1, rp2])
    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()