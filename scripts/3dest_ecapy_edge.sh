#!/usr/bin/env bash

echo "Destroy running ecapy container"
docker stop ecapy
docker rm -f ecapy

