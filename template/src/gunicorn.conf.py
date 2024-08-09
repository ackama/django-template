GUNICORN_LOG_LEVEL = "info"

# Server Socket
bind = "0.0.0.0:8000"

# Worker Processes
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"

# Logging
loglevel = GUNICORN_LOG_LEVEL
accesslog = "-"  # Log to stdout
errorlog = "-"  # Log to stderr
