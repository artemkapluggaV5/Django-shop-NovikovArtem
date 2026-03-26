from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from .cart_utils import update_cart_item
from .forms import CartAddProductForm
from .models import CartItem


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'update': True
        })
    return render(request, 'cart/detail.html', {'cart': cart})


class FrontCartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        try:
            quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            quantity = 1
        cart.add(product=product, quantity=quantity, update_quantity=True)
        return redirect('frontend-cart-detail')


class FrontCartDetailView(View):
    template_name = 'catalog/users/cart_detail.html'

    def get(self, request):
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart_items = []
        return render(request, self.template_name, {'cart': cart_items})