FROM python:3.11-slim AS base

#WORKDIR /app
WORKDIR /server/
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "server.py"]

#FROM base AS test
#CMD ["python", "-m", "unittest", "discover"]
