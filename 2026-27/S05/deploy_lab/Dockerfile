# A recipe for the box: start from a slim Python, install the exact libraries, copy the model and the app,
# and start the API. "docker build" turns this into an image; "docker run" starts a container from it.
FROM python:3.11-slim

WORKDIR /app

# Install dependencies first so Docker can cache this layer when only the code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the trained model and the API code.
COPY churn_model.pkl app.py ./

# Cloud Run (and most platforms) send traffic to the port in $PORT; default to 8080 locally.
ENV PORT=8080
EXPOSE 8080

# Start the API. Shell form so $PORT is expanded.
CMD uvicorn app:app --host 0.0.0.0 --port ${PORT}
