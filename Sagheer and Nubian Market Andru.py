

n, S = list(map(int, input().split(' ')))
prices = list(map(int, input().split(' ')))
prices.sort(reverse=True)


def calculate_price(cart):
    price = 0
    for i in range(len(cart)):
        price += cart[i] + ((i + 1) * len(cart))
    return price

cart = []

while calculate_price(cart) <= S and prices:
    cart.insert(0, prices.pop())

if calculate_price(cart) > S:
    cart = cart[1:]

print(len(cart), calculate_price(cart))

