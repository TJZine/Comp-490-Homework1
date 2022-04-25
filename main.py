from dataclasses import dataclass

@dataclass
class CartItem:
    name: str
    item_type: str
    item_price: float
    state_purchased: str
    quantity: int = 0

    def total_cost(self) -> float:
        if self.item_type.lower() == ('everything else' or 'everythingelse'):
            print("everything")
            return self.total_cost_else()
        elif self.item_type.lower() == ('wic eligible food' or 'wiceligiblefood'):
            print("food")
            return self.total_cost_food()
        elif self.item_type.lower() == 'clothing':
            print("clothes")
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


def create_cart_items() -> list[CartItem]:
    cart_items: list[CartItem]
    cart_items = [CartItem('bread', 'Wic Eligible Food', 3.99, 'ma', 2),
                  CartItem('milk', 'Wic Eligible Food', 4.79, 'ma', 1),
                  CartItem('eggs', 'Wic Eligible Food', 2.89, 'me', 1),
                  CartItem('jeans', 'clothing', 29.99, 'ma', 1),
                  CartItem('hoodie', 'clothing', 79.99, 'ma', 2)]
    return cart_items


def cart_total(cart_items: list[CartItem]) -> float:
    total = 0
    ma_clothing_subtotal = 0
    for item in cart_items:
        if item.item_type.lower() == 'clothing' and item.state_purchased.lower() == 'ma':
            ma_clothing_subtotal += item.total_cost()
        total += item.total_cost()
    if ma_clothing_subtotal > 175:
        total += ((ma_clothing_subtotal - 175) * .0625)
    return total


if __name__ == '__main__':
    cart = create_cart_items()
    print(cart_total(cart))


