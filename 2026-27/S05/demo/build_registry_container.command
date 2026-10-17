#!/bin/bash
# Session 5 · Demo 2 preparation: build a container from the model registry (run ONCE, the day before).
#
# Takes the model that the Session 3 MLflow registry marks as "production"
# (models:/churn-model@production = version 1) and builds a Docker image that serves it.
# In class you only START this image; you do not build it (the build downloads ~1 GB and takes a few minutes).
#
# Needs: Rancher Desktop running with the "dockerd (moby)" container engine, and the Session 3
# environment (S03/demo/mlflow/.venv, created by start_mlflow_ui.command).
cd "$(dirname "$0")"
HERE="$(pwd)"
S3="$HERE/../../S03/demo/mlflow"

if ! command -v docker >/dev/null 2>&1; then
  echo "The 'docker' command was not found."
  echo "In Rancher Desktop: Preferences -> Container Engine -> choose 'dockerd (moby)', apply, wait until it says Ready."
  exit 1
fi
if ! docker info >/dev/null 2>&1; then
  echo "Docker is installed but the engine is not running. Open Rancher Desktop and wait until it says Ready, then run this again."
  exit 1
fi
if [ ! -x "$S3/.venv/bin/mlflow" ]; then
  echo "The Session 3 environment was not found. Double-click S03/demo/mlflow/start_mlflow_ui.command once, stop it with Ctrl+C, and run this again."
  exit 1
fi

cd "$S3"
echo "1/3  Asking the registry which model is 'production'..."
# The registry entry points at the run that trained the model; the model files themselves live in that
# run's logged model (mlruns/churn-model/models/m-...). Resolve alias -> version -> logged model.
MODEL_URI=$(MLFLOW_TRACKING_URI=sqlite:///mlflow.db ./.venv/bin/python - 2>/dev/null <<'PY'
import mlflow
from mlflow import MlflowClient
c = MlflowClient()
mv = c.get_model_version_by_alias("churn-model", "production")
exp = c.get_run(mv.run_id).info.experiment_id
found = mlflow.search_logged_models(experiment_ids=[exp], filter_string=f"source_run_id = '{mv.run_id}'", output_format="list")
found = [m for m in found if m.name == "model"] or found
print(f"version {mv.version} -> models:/{found[0].model_id}")
PY
)
if [ -z "$MODEL_URI" ]; then echo "Could not resolve models:/churn-model@production in the Session 3 registry."; exit 1; fi
echo "     churn-model @production = $MODEL_URI"
MODEL_URI="${MODEL_URI##*-> }"

echo "     Copying that model out of the registry into S05/demo/registry_box/model ..."
BOX="$HERE/registry_box"
rm -rf "$BOX"; mkdir -p "$BOX"
MLFLOW_TRACKING_URI=sqlite:///mlflow.db ./.venv/bin/mlflow artifacts download \
    -u "$MODEL_URI" -d "$BOX/model" >/dev/null 2>&1 || { echo "Could not copy the model out of the registry."; exit 1; }
[ -f "$BOX/model/MLmodel" ] || { echo "The copied model has no MLmodel file."; exit 1; }
# The recipe for the box. Built natively for this Mac's chip ('mlflow models build-docker' forces an
# Intel image, which crashes under emulation on Apple-silicon Macs).
cat > "$BOX/Dockerfile" <<'DOCKERFILE'
# The recipe for the box: a slim Python, the model's exact libraries, the model, and MLflow's web server.
FROM python:3.10.12-slim
WORKDIR /opt/ml
COPY model/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY model /opt/ml/model
ENV MLFLOW_DISABLE_TELEMETRY=true
EXPOSE 8080
CMD ["mlflow", "models", "serve", "-m", "/opt/ml/model", "--env-manager", "local", "-h", "0.0.0.0", "-p", "8080"]
DOCKERFILE
echo "     Building the image churn-model:production (3-6 minutes the first time)..."
LOG="$HERE/build_registry_container.log"
set -o pipefail
docker build -t churn-model:production "$BOX" 2>&1 | tee "$LOG" \
    || { echo; echo "Build failed. The full log is in S05/demo/build_registry_container.log"; exit 1; }
cd "$HERE"

echo
echo "2/3  Starting it once to test (port 5002)..."
docker rm -f churn-prod >/dev/null 2>&1 || true
docker run -d -p 5002:8080 --name churn-prod churn-model:production >/dev/null
for i in $(seq 1 30); do
  [ "$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:5002/ping)" = "200" ] && break
  sleep 2
done
echo "   ping       : HTTP $(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:5002/ping)   (200 = alive)"
echo "   prediction : $(curl -s -X POST http://127.0.0.1:5002/invocations -H 'Content-Type: application/json' -d @customers.json)"
echo "                expected: {\"predictions\": [0, 1]}   (loyal customer stays, at-risk customer leaves)"

echo
echo "3/3  Stopping the test container (the image stays, ready for class)..."
docker rm -f churn-prod >/dev/null
docker images churn-model
echo
echo "Done. In class, use the commands in class_commands.txt."
