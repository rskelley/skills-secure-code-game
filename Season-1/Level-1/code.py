'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    MAX_AMOUNT = 100000000
    net = 0.0
    total_items = 0.0
    total_payments = 0.0
    for item in order.items:
        amount = round(item.amount * 100,0)
        if item.type == 'payment':
            total_payments  += amount
        elif item.type == 'product':
            amount = amount * item.quantity
            if -MAX_AMOUNT < amount < MAX_AMOUNT:
                total_items += round(amount,0)
        else:
            return "Invalid item type: %s" % item.type
    net = total_payments - total_items
    net = round(net/100,2)
    if net > 0:
        return "Total amount payable for an order exceeded"
    elif net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id