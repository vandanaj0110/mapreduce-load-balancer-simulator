#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line = line.strip()
    parts = line.split()
    if len(parts)==4:
       parts.append('0.0')
    if len(parts) == 5:
        request_id, client_id, endpoint, timestamp, no_of_servers_down = parts
        print(f"{request_id} {client_id} {endpoint} {timestamp} {no_of_servers_down}")
    elif len(parts) == 2:
        request_idp, predicted_status_code = parts
        print(f"{request_idp} {predicted_status_code}")

