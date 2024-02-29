#!/bin/bash
# send DELETE request to URL passed as first argument and displays the body of the response
curl -sX DELETE "$1"
