#!/usr/bin/env python3
import sys
for line in sys.stdin:
	parts=line.strip().split()
	request_id, client_id, endpoint, timestamp, assigned_server, predicted_status_code, result = parts
	print(f"{client_id} {request_id} {endpoint} {timestamp} {assigned_server} {predicted_status_code}")
	

