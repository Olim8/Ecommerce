from django.shortcuts import render
from cart.cart import Cart
from payments.forms import ShippingForm
from payments.models import ShippingAddress


def payment_success(request):
    return render(request, 'payments/payment_success.html', {})


def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    if request.user.is_authenticated:
        # Checkout as logged in user
        # Shipping User
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        # Shipping Form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "payments/checkout.html", {'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form})
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "payments/checkout.html", {'cart_products':cart_products, 'quantities':quantities, 'totals':totals, 'shipping_form':shipping_form})