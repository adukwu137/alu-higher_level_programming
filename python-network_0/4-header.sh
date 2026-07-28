#!/bin/bash
# Sends a GET request to the URL with header X-HolbertonSchool-User-Id: 98
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
