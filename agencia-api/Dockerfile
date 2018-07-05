FROM python-base:latest

COPY requirements.txt /app/requirements.txt

RUN pip3 install --no-cache-dir -r /app/requirements.txt

COPY app /app
COPY config /config
COPY run.py /run.py

COPY tests /tests
RUN pip3 install --no-cache-dir -r /tests/requirements.txt
COPY test.py /test.py
RUN python test.py
RUN pip3 uninstall -y -r /tests/requirements.txt
RUN rm /test.py
RUN rm -rf /tests

ENV PORT 8109
EXPOSE $PORT
