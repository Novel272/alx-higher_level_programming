#!/bin/bash
# displays all HTTP methods server will try to accept using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
