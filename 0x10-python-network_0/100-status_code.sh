#!/bin/bash
#transmit a GET request to the provided URL and outputs the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
