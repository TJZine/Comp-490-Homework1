from dataclasses import dataclass


@dataclass
class CartItem:
    name: str
    item_type: str
    item_price: float
    quantity: int = 0
    state_purchased: str = ''

    def total_cost(self) -> float:
        if self.item_price <= 0:
            raise ValueError('Cart Item at or Below 0.00.')
        if self.item_type.lower() == 'everything else':
            return self.total_cost_else()
        elif self.item_type.lower() == 'wic eligible food':
            return self.total_cost_food()
        elif self.item_type.lower() == 'clothing':
            return self.total_cost_clothing()

    def total_cost_else(self) -> float:
        subtotal = self.item_price * self.quantity
        if self.state_purchased.lower() == "ma":
            return subtotal + (subtotal * .0625)
        elif self.state_purchased.lower() == "me":
            return subtotal + (subtotal * .0525)
        else:
            return subtotal

    def total_cost_food(self) -> float:
        subtotal = self.item_price * self.quantity
        return subtotal

    def total_cost_clothing(self) -> float:
        subtotal = self.item_price * self.quantity
        if self.state_purchased.lower() == "me":
            return subtotal + (subtotal * .0525)
        else:
            return subtotal

    def set_user_state(self, state):
        self.state_purchased = state


def create_cart_items() -> list[CartItem]:
    cart_items: list[CartItem]
    cart_items = [CartItem('bread', 'Wic Eligible Food', 3.99, 2),
                  CartItem('milk', 'Wic Eligible Food', 4.79, 1),
                  CartItem('eggs', 'Wic Eligible Food', 2.89, 1),
                  CartItem('jeans', 'clothing', 29.99, 1),
                  CartItem('hoodie', 'clothing', 79.99, 3),
                  CartItem('t-shirt', 'clothing', 22.49, 3),
                  CartItem('video game', 'everything else', 59.99, 1),
                  CartItem('fishing rod', 'everything else', 99.99, 1),
                  CartItem('cell phone', 'everything else', 599.99, 1)]
    return cart_items


def check_state_input(state: str):
    allowed_states = ['ma', 'me', 'nh']
    print(state.lower())
    if state.lower() not in allowed_states:
        raise ValueError('Only allowed states are MA, ME, and NH')


def cart_total(cart_items: list[CartItem], state: str) -> float:
    total, ma_clothing_subtotal = 0, 0
    check_state_input(state)
    for item in cart_items:
        item.set_user_state(state)
        # if item.item_price <= 0:
        #    raise ValueError('Cart Item at or Below 0.00.')
        if item.item_type.lower() == 'clothing' and item.state_purchased.lower() == 'ma':
            ma_clothing_subtotal += item.total_cost()
        total += item.total_cost()
    if ma_clothing_subtotal > 175:
        total += ((ma_clothing_subtotal - 175) * .0625)
    return round(total, 2)

    
if __name__ == '__main__':
    cart = create_cart_items()
    print(cart_total(cart, 'MA'))
    print(cart_total(cart, 'ME'))
    print(cart_total(cart, 'NH'))
