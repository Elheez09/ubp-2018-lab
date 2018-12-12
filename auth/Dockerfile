FROM alpine:latest

RUN apk add --update build-base python2-dev libffi-dev openssl-dev
RUN apk add --update py-pip
RUN pip install --upgrade pip
ADD . /usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8081

CMD ["python", "/usr/src/app/auth-svc/app.py"]
