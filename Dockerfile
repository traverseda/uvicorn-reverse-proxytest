from python as base

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
