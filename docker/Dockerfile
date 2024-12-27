# Stage 1: Build dependencies
FROM python:3.10.5-slim-buster AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Build final image
FROM python:3.10.5-slim-buster

WORKDIR /app

# Copy dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the rest of the application code into the container
COPY . .

# Expose the port the app will run on
EXPOSE 8000
COPY ./docker/run.sh run.sh

CMD ["bash", "scripts/run.sh"]
