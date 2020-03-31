from shopping_list import app, db

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


    def __repr__(self):
        return f'{self.quantity} {self.item}s have been added to the cart'