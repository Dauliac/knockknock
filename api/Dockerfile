############################
# Date        : Sat 02 Jun 2018 12:48:37 AM CEST
# Version     : 0.0.1
# Description : 0.0.1
FROM python:3.5-alpine

WORKDIR /usr/src
ADD . /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN ln -sf /usr/src/webui/index.html /usr/src/app/templates/index.html
RUN ln -sf /usr/src/webui/static /usr/src/app/static

COPY . .
EXPOSE 5000

# Run
CMD ["python", "./main.py"]

