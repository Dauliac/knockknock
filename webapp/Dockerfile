############################
# Date        : Sat 02 Jun 2018 12:48:37 AM CEST
# Version     : 0.0.1
# Description : 0.0.1
FROM python:3.5-alpine

WORKDIR /usr/src
ADD . /usr/src

COPY requirements.txt ./
RUN apk update && apk add bash
RUN pip install --no-cache-dir -r requirements.txt
# RUN rm -rfv /usr/src/webui/static
# RUN rm -rfv /usr/src/webui/index.html

EXPOSE 5000

# Run
CMD ["python", "./app.py"]

