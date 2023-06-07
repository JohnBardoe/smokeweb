FROM python:3.10-slim-buster
WORKDIR /usr/src/app

COPY . .
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

CMD [ "python3", "app.py"]
