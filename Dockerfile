FROM python:3.8
RUN mkdir /opt/app
COPY app.py /opt/app
WORKDIR /opt/app
CMD ["python3", "app.py"]
