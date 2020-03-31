from shopping_list import app, db

from flask import render_template, redirect, request, url_for

from shopping_list.forms import ShoppingForm

from shopping_list.models import Cart


@app.route('/', methods=['GET', 'POST'])
def home():
    form = ShoppingForm()
    if request.method == 'POST' and form.validate():
        item = form.item.data
        quantity = form.quantity.data
        print(f'Item: {item}\nQuantity: {quantity}')

        db.session.add(Cart(item, quantity))
        db.session.commit()
    return render_template('home.html', form=form)
    

@app.route('/cart', methods=['GET'])
def get_cart():
    cart = Cart.query.all()
    return render_template('cart.html', cart=cart)
    

@app.route('/cart/update/<int:cart_id>', methods=['GET', 'POST'])
def update_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)

    updateCart = ShoppingForm()
    if request.method == 'POST' and updateCart.validate():
        item = updateCart.item.data
        quantity = updateCart.quantity.data

        cart.item = item
        cart.quantity = quantity

        db.session.commit()
        return redirect(url_for('get_cart'))
    return render_template('update_cart.html', form=updateCart)
    

@app.route('/cart/<int:cart_id>')
def cart_detail(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    return render_template('cart_detail.html', cart=cart)
    

@app.route('/cart/delete/<int:cart_id>')
def delete_from_cart(cart_id):
    cart = Cart.query.get_or_404(cart_id)
    db.session.delete(cart)
    db.session.commit()
    return redirect(url_for('get_cart'))