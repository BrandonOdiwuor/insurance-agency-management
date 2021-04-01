#!/usr/bin/env bash
set -e
docker-compose -f docker-local-stack.yml down -v --rmi local