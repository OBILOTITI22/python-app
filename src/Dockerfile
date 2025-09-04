FROM python:3.10-alpine

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY src/ /src/

# Make sure you're in the right directory when running.
WORKDIR /src

CMD ["python", "app.py"]