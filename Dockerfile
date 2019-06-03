FROM python:3.7

LABEL maintainer="aleksey@kolyadin.ru"

RUN apt-get update && apt-get install -y libzbar-dev
RUN pip install opencv-python pyzbar Flask gevent

COPY microservice.py /var/www/html/
COPY extractor.py /var/www/html/
COPY optimizer.py /var/www/html/

CMD ["python", "/var/www/html/microservice.py"]
