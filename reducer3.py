#!/usr/bin/env python3
import sys

def main():
    current_client = None
    correct_predictions = 0
    total_requests = 0
    total_price = 0
    for line in sys.stdin:
        client_id,request_id,endpoint,timestamp,actual_status,predicted_status_code= line.strip().split()
        if current_client and current_client != client_id:
            print(f"{current_client} {correct_predictions}/{total_requests} {total_price}")
            correct_predictions = 0
            total_requests = 0
            total_price = 0
        current_client = client_id
        total_requests += 1
        if predicted_status_code == actual_status:
            correct_predictions += 1
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
        if(actual_status=='200'):
        	total_price += endpoint_prices.get(endpoint, 0)  
    if current_client:
        print(f"{current_client} {correct_predictions}/{total_requests} {total_price}")

if __name__ == "__main__":
    main()

	

