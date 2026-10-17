MLOps · Session 5 lab · From the registry to a container

This folder is a model taken out of the course's MLflow model registry
(churn-model, version 1, alias "production"), plus the recipe to put it in a box.

  model/            the model exactly as the registry stores it (MLmodel, model.skops, requirements.txt, ...)
  Dockerfile        the recipe for the box (eight lines)
  customers.json    two customers to send to the model
  my_customer.json  one customer for you to change

Full step-by-step instructions: MLOps_S05_Registry_to_Container_Lab.pdf (on the campus).

The short version, in a terminal opened in this folder:
  docker build -t churn-model:production .
  docker run -d -p 5002:8080 --name churn-prod churn-model:production
  curl -s -X POST http://localhost:5002/invocations -H "Content-Type: application/json" -d @customers.json
  docker rm -f churn-prod
