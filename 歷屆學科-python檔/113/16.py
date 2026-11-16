# -*- coding: utf-8 -*-

orders = [100, 150, 200, 80, 120]
avg_orders = sum(orders) / len(orders)
below_avg = [o for o in orders if o < avg_orders]
print (len(below_avg) % 4)
