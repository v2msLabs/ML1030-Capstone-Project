#FROM ubuntu:18.04
FROM python:3.6.7

RUN pip3 install --upgrade pip==19.2.3 \
    && pip3 install setuptools

# for flask web server
EXPOSE 5000

# set working directory

WORKDIR .
COPY requirements.txt .

ENV FLASK_ENV development
ENV FLASK_APP example

# install required libraries
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod 644 app.py

# Run app.py when the container launches
CMD ["python3","app.py"]