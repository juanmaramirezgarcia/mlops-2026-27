#!/bin/bash
# Double-click in Finder (or run in Terminal) to build the container and run the churn API on your Mac.
# Needs Docker Desktop running and Python 3. Stop the API with:  docker rm -f churn-api
cd "$(dirname "$0")"
set -e

echo "1/4  Training the model (once)..."
[ -f churn_model.pkl ] || python3 train.py

echo "2/4  Building the image (docker build)..."
docker build -t churn-api:v1 .

echo "3/4  Starting the container (docker run -p 8080:8080)..."
docker rm -f churn-api 2>/dev/null || true
docker run -d -p 8080:8080 --name churn-api churn-api:v1 >/dev/null

echo "4/4  Waiting for the API, then testing it..."
sleep 3
echo "   health : $(curl -s http://127.0.0.1:8080/health)"
echo "   predict: $(curl -s -X POST http://127.0.0.1:8080/predict -H 'Content-Type: application/json' \
                    -d '{"tenure_months":6,"monthly_charges":85,"support_tickets":4,"promo_weeks_last_quarter":1,"is_monthly":1,"region_north":1}')"
echo
echo "The API is running. Open the interactive docs:  http://127.0.0.1:8080/docs"
open "http://127.0.0.1:8080/docs" 2>/dev/null || true
echo "Stop it when you are done with:  docker rm -f churn-api"
