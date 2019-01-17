"""
Unlike a model, items placed n the cart will
not be stored in DB - but added to a session
when a user is logged in. Cart is cleared
after logout.
"""
from django.shortcuts import get_list_or_404

from products.models import Product

def cart_contents(request):
    """
    Display aitems added to the cart 
    """

    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0

    for id, quantity in cart_items():
        product = get_list_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({"id": id, "quantity": quantity, "product": product})

        return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
