from dataclasses import dataclass
from typing import Final

state_tax: Final = {'ma': .0625, 'me': .0525, 'nh': 0.0}


@dataclass
class CartItem:
    name: str
    item_type: str
    __item_price: float

    def total_cost(self) -> float:
        if self.__item_price <= 0:
            raise ValueError('Cart Item at or Below 0.00.')
        else:
            return self.__item_price


def create_cart_items() -> list[CartItem]:
    cart_items: list[CartItem]
    cart_items = [CartItem('bread', 'Wic Eligible Food', 3.99),
                  CartItem('milk', 'Wic Eligible Food', 4.79),
                  CartItem('eggs', 'Wic Eligible Food', 2.89),
                  CartItem('jeans', 'clothing', 29.99),
                  CartItem('hoodie', 'clothing', 79.99),
                  CartItem('t-shirt', 'clothing', 22.49),
                  CartItem('video game', 'everything else', 59.99),
                  CartItem('fishing rod', 'everything else', 99.99),
                  CartItem('cell phone', 'everything else', 599.99)]
    return cart_items


def check_state_input(state: str):
    if state not in state_tax.keys():
        raise ValueError('Only allowed states are MA, ME, and NH')


def clothing_tax(item: CartItem, state: str) -> float:
    if state == "me":
        return item.total_cost() + calculate_tax(item, state)
    else:
        return item.total_cost()


def everything_else_tax(item: CartItem, state: str) -> float:
    if state == 'nh':
        return item.total_cost()
    else:
        return item.total_cost() + calculate_tax(item, state)


def taxed_total(item: CartItem, state: str) -> float:
    if item.item_type.lower() == 'wic eligible food':
        return item.total_cost()
    elif item.item_type.lower() == 'clothing':
        return clothing_tax(item, state)
    elif item.item_type.lower() == 'everything else':
        return everything_else_tax(item, state)


def calculate_tax(item: CartItem, state: str) -> float:
    tax = 0
    if state in state_tax.keys():
        tax = item.total_cost() * state_tax.get(state)
    return tax


def cart_total(cart_items: list[CartItem], state: str) -> float:
    total, ma_clothing_subtotal = 0, 0
    state = state.lower()
    check_state_input(state)
    for item in cart_items:
        if item.item_type.lower() == 'clothing' and state == 'ma':
            ma_clothing_subtotal += item.total_cost()
        total += taxed_total(item, state)
    if ma_clothing_subtotal > 175:
        total += ((ma_clothing_subtotal - 175) * state_tax.get('ma'))
    return round(total, 2)


if __name__ == '__main__':
    cart = create_cart_items()
    print(cart_total(cart, 'MA'))
    print(cart_total(cart, 'ME'))
    print(cart_total(cart, 'NH'))
