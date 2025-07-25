#!/usr/bin/env python3
import sys

# Define endpoint prices
endpoint_prices = {
    'user/profile': 100,
    'user/settings': 200,
    'order/history': 300,
    'order/checkout': 400,
    'product/details': 500,
    'product/search': 600,
    'cart/add': 700,
    'cart/remove': 800,
    'payment/submit': 900,
    'support/ticket': 1000
}
for line in sys.stdin:
    line = line.strip()
    parts=line.split()
    request_id, client_id, endpoint, timestamp, no_of_servers_down, predicted_sc = parts
    print(f"{timestamp} {request_id} {endpoint} {client_id} {no_of_servers_down} {predicted_sc}")
