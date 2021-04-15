#!/usr/bin/env bash
set -e
docker-compose -f docker/docker-compose.yml config > docker-compose.yml
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml down
docker-compose -f docker-compose.yml up