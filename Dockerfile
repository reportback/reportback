FROM python:3.9.6-slim-buster

# Hopefully, dependencies should be relatively stable, so builds can be faster
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY ./app /app
# dot files are ignored by default
COPY .env /

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]