from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def home(request):
    return render(request, 'home.html', context={'current_tab': 'home'})


def collections(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)

        # Create a cart in the session if it doesn't exist
        if 'cart' not in request.session:
            request.session['cart'] = {}

        # Add or update the product in the cart
        if product_id in request.session['cart']:
            request.session['cart'][product_id]['quantity'] += quantity
        else:
            request.session['cart'][product_id] = {
                'name': product.name,
                'price': str(product.price),  # Store as string for JSON serialization
                'image': product.image.url,
                'quantity': quantity,
            }

        request.session.modified = True
        return redirect('cart')

    return render(request, 'collections.html', {'products': products})


def cart(request):
    cart_items = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items.values())
    return render(request, 'cart.html', {'cart_items': cart_items.values(), 'total_price': total_price})


def checkout(request):
    if request.method == 'POST':
        # Capture form data
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        payment_option = request.POST.get('payment_option')


        Checkout.objects.create(
            name=name,
            phone_number=phone_number,
            address=address,
            city=city,
            pincode=pincode,
            payment_option=payment_option,
        )
        return redirect('checkout_success')

    return render(request, 'checkout.html', {})

def checkout_success(request):
    return render(request, 'checkout_success.html', {})

