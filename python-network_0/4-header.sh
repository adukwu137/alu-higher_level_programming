#!/bin/bash
# Sends a GET request to the URL with the required user ID header
curl -s -H "X-HolbertonSchool-User-Id: 98" -H "X-School-User-Id: 98" "$1"
