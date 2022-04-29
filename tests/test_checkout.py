import pytest
import checkout


def create_food_list():
    cart_items: list[checkout.CartItem]
    cart_items = [checkout.CartItem('bread', 'Wic Eligible Food', 3.99),
                  checkout.CartItem('cheese', 'Wic Eligible Food', 2.99),
                  checkout.CartItem('cereal', 'Wic Eligible Food', 4.79)]
    return cart_items


def test_total_cost_food():
    cart = create_food_list()
    total_ma = checkout.cart_total(cart, 'MA')
    total_me = checkout.cart_total(cart, 'ME')
    total_nh = checkout.cart_total(cart, 'NH')
    assert (total_ma and total_me and total_nh) == 11.77


def create_clothing_list():
    cart_items: list[checkout.CartItem]
    cart_items = [checkout.CartItem('sweatpants', 'clothing', 29.99),
                  checkout.CartItem('jacket', 'clothing', 89.99),
                  checkout.CartItem('jeans', 'clothing', 59.99),
                  checkout.CartItem('t-shirt', 'clothing', 22.49)]
    return cart_items


def test_total_cost_clothing():
    cart = create_clothing_list()
    total_ma = checkout.cart_total(cart, 'ma')
    assert total_ma == 204.18
    total_me = checkout.cart_total(cart, 'me')
    assert total_me == 213.09
    total_nh = checkout.cart_total(cart, 'nh')
    assert total_nh == 202.46


def create_misc_list():
    cart_items: list[checkout.CartItem]
    cart_items = [checkout.CartItem('movie', 'everything else', 24.99),
                  checkout.CartItem('Headphones', 'everything else', 97.99),
                  checkout.CartItem('gift-card', 'everything else', 20.00)]
    return cart_items


def test_total_cost_else():
    cart = create_misc_list()
    total_ma = checkout.cart_total(cart, 'ma')
    assert total_ma == 151.92
    total_me = checkout.cart_total(cart, 'me')
    assert total_me == 150.49
    total_nh = checkout.cart_total(cart, 'nh')
    assert total_nh == 142.98


def create_bad_list():
    cart_items: list[checkout.CartItem]
    cart_items = [checkout.CartItem('movie', 'everything else', 24.99),
                  checkout.CartItem('Headphones', 'everything else', 0.00),
                  checkout.CartItem('gift-card', 'everything else', -20.00)]
    return cart_items


def test_bad_input_total_cost():
    cart = create_bad_list()
    cart_zero = [cart[1]]
    cart_negative = [cart[2]]
    with pytest.raises(ValueError):
        total = checkout.cart_total(cart, 'ma')
    with pytest.raises(ValueError):
        total2 = checkout.cart_total(cart_zero, 'me')
    with pytest.raises(ValueError):
        total3 = checkout.cart_total(cart_negative, 'nh')


def create_empty_list():
    cart_items: list[checkout.CartItem]
    cart_items = []
    return cart_items


def test_empty_cart():
    cart = create_empty_list()
    total = checkout.cart_total(cart, 'ma')
    assert total == 0


def test_unsupported_state():
    cart = create_misc_list()
    with pytest.raises(ValueError):
        total = checkout.cart_total(cart, 'CA')
