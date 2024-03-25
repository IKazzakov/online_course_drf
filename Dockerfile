FROM ubuntu:latest
LABEL authors="igor-mint"

ENTRYPOINT ["top", "-b"]

FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
