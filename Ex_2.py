prices = {
    "bananas": 4,
    "apples": 2,
    "oranges": 1.5,
    "pears": 3

}
stock = {
    "bananas": 6,
    "apples": 0,
    "oranges": 32,
    "pears": 15

}
for i, j in zip(prices, stock):
    print(i)
    print("price : ", prices[i])
    print("stock : " , stock[i])

total = 0
for i, j in zip(prices, stock):
    item_prices = prices[i]*stock[i]
    total += item_prices
    print("The price of all", i,"is", item_prices)
print(total)