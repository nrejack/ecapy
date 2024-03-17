#!/usr/bin/env bash

echo "Running ec container from edge"
docker run -p 5000:5000 -d --rm --name  ecapy nrejack/ecapybara:edge

