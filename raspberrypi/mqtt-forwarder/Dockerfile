FROM python:3.7
RUN pip3 install paho-mqtt==1.5.0 influxdb==5.2.3

ADD python-listener.py /
CMD ["python3", "/python-listener.py"]