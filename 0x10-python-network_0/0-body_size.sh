#!/bin/bash
# send request to URL with curl, and display size of body of response
curl -s "$1" | wc -c
