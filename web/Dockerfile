from alpine:latest
RUN apk add --update nodejs nodejs-npm
ADD . /usr/src/app/
WORKDIR /usr/src/app/web-svc
RUN npm install express-handlebars express express-session body-parser jsonwebtoken fs request crypto-js nodemon
EXPOSE 8080
CMD ["npm", "run", "live"]
