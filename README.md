# ML Inference Lab

Flask app for mock ML inference, containerized with Docker.

## Build

```bash
docker build -t inference-service:v1 .
```

## Run

```bash
docker run -d -p 5001:5001 --name inference-service inference-service:v1
```

## Test

```bash
curl -X POST http://localhost:5001/predict -H "Content-Type: application/json" -d '{"features":[1,2,3]}'
```

**Expected Output:**
```json
{"prediction":"mock_prediction"}
```

## Stop

```bash
docker stop inference-service
docker rm inference-service
```


# Lab Reflection

Dockerizing the Flask app was mostly okay, but I hit a Werkzeug version clash that broke imports until I pinned Werkzeug to 2.2.3. Switching to port 5001 because 5000 was taken locally meant updating `app.py` and the `Dockerfile`, which was a bit annoying. The `python:3.9-slim` image kept the image size decent, but dependencies added some bulk.

In production, cloud setups like AWS EKS would cost more with VM and Kubernetes fees compared to local Docker. GPUs for inference would speed things up but get pricey fast. Autoscaling in Kubernetes could save money by matching resources to demand, but it’d need careful setup.