FROM nginx:alpine

ENV LISTEN_PORT $PORT

WORKDIR /usr/share/nginx

COPY . .

EXPOSE $PORT

CMD nginx -g 'daemon off;'
