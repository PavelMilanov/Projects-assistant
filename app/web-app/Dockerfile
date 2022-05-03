FROM node:14.17.6 as build

COPY ./ .
RUN npm install
RUN npm run build

FROM nginx:stable

RUN mkdir /www
COPY --from=build dist/ www/
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
