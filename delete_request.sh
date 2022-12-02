#! /usr/bin/bash

netcat 127.0.0.1 8000 < delete_request_chargepoint.txt
# netcat 127.0.0.1 8000 < delete_request_customer.txt