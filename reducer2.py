#!/usr/bin/env python3
import sys

def convert_to_seconds(timestamp):
    hours, minutes, seconds = map(int, timestamp.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def main():
    current_timestamp = None
    clients_at_timestamp = set()
    endpoint_servers = {
        'user/profile': [True, True, True],
        'user/settings': [True, True, True],
        'order/history': [True, True, True],
        'order/checkout': [True, True, True],
        'product/details': [True, True, True],
        'product/search': [True, True, True],
        'cart/add': [True, True, True],
        'cart/remove': [True, True, True],
        'payment/submit': [True, True, True],
        'support/ticket': [True, True, True]
    }
    server_assignment_time = {endpoint: [-1, -1, -1] for endpoint in endpoint_servers}
    available_servers_count = {endpoint: 3 for endpoint in endpoint_servers}

    for line in sys.stdin:
        timestamp, request_id, endpoint, client_id, no_of_servers_down, predicted_status_code = line.strip().split()
        if timestamp != current_timestamp:
            current_time_seconds = convert_to_seconds(timestamp)
            current_timestamp = timestamp
            clients_at_timestamp.clear()
        if client_id in clients_at_timestamp:
            continue
        clients_at_timestamp.add(client_id)

        for i in range(3):
            if not endpoint_servers[endpoint][i] and server_assignment_time[endpoint][i] != -1:
                if current_time_seconds - server_assignment_time[endpoint][i] >= 1:
                    endpoint_servers[endpoint][i] = True
                    server_assignment_time[endpoint][i] = -1
                    available_servers_count[endpoint] += 1

        if available_servers_count[endpoint] > int(float(no_of_servers_down)):
            for i in range(3):
                if endpoint_servers[endpoint][i]:
                    endpoint_servers[endpoint][i] = False  # Mark server as down
                    server_assignment_time[endpoint][i] = current_time_seconds 
                    available_servers_count[endpoint] -= 1
                    print(f"{request_id} {client_id} {endpoint} {timestamp} 200 {predicted_status_code} Accepted")
                    break
        else:
            print(f"{request_id} {client_id} {endpoint} {timestamp} 500 {predicted_status_code} Rejected")

if __name__ == "__main__":
    main()

