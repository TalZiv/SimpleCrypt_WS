FROM python:3.6
WORKDIR /app
COPY requirements.txt ./
COPY simplecrypt-tools_unit_test.py ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pytest /app/simplecrypt-tools_unit_test.py

FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY SimpleCrypt_WS.py ./main.py