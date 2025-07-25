#!/usr/bin/env python3
import sys

def main():
    current_city = None
    profit_count = 0
    loss_count = 0
    for line in sys.stdin:
    	line = line.strip()
    	parts = line.split()
    	if len(parts)==2:
    	   a=parts[1]
    	elif len(parts)==5:
    		parts.append(a)
    		request_id, client_id, endpoint, timestamp, no_of_servers_down, predicted_sc = parts
    		print(f"{request_id} {client_id} {endpoint} {timestamp} {no_of_servers_down} {predicted_sc}")

if __name__ == "__main__":
    main()

