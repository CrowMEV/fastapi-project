#!bin/sh
alembic upgrade head && gunicorn app.main:app --workers 2 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0