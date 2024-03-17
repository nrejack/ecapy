#!/usr/bin/env bash

echo "Building ec container from edge"
cd ..
docker build . -t nrejack/ecapybara:edge
cd scripts/

