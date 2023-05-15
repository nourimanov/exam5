FROM python:3.11-alpine

WORKDIR /apps
COPY . /apps
RUN pip install -r requirement.txt

ENTRYPOINT ["python", "main.py"]
