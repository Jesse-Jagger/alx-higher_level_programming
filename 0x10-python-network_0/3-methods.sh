#!/bin/bash
# Displays all HTTP methods of the server for a provided URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
