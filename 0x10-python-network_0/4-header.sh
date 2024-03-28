#!/bin/bash

# transmits a GET request to a provided URL with the header variable.
curl -sH "X-School-User-Id: 98" "$1"
