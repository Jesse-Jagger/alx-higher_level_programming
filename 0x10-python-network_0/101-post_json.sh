#!/bin/bash
#sends a JSON POST request to a provided URL and displays the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
