from catalog.models import Product
from .models import CartItem

def add_to_cart(user, product, quantity):
    item, created = CartItem.objects.get_or_create(user=user, product=product)
    item.quantity += quantity
    item.save()
    return item

def update_cart_item(user, product, quantity):
    item = CartItem.objects.filter(user=user, product=product).first()
    if item:
        item.quantity = quantity
        item.save()
        return item
    return None