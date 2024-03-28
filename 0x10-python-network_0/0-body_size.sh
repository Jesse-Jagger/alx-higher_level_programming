#!/bin/bash

# Gets the byte size of an HTTP response header for a provided URL.

curl -s "$1" | wc -c
