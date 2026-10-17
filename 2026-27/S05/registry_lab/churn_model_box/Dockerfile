# The recipe for the box: a slim Python, the model's exact libraries, the model, and MLflow's web server.
FROM python:3.10.12-slim
WORKDIR /opt/ml
COPY model/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY model /opt/ml/model
ENV MLFLOW_DISABLE_TELEMETRY=true
EXPOSE 8080
CMD ["mlflow", "models", "serve", "-m", "/opt/ml/model", "--env-manager", "local", "-h", "0.0.0.0", "-p", "8080"]
