#!/bin/bash

# Check if the URL is provided
if [[ $# -ne 1 ]]; then
  echo "Usage: ./0-body_size.sh <URL>"
  exit 1
fi

# Get the size of the body of the response
response_size=$(curl -s -o /dev/null -w "%{content_length}" -X GET $1)

# Display the size of the body of the response
echo "$response_size"

