FROM nginx:alpine

WORKDIR /usr/share/nginx

COPY conf.d/default.conf.template /etc/nginx/conf.d/default.conf.template

COPY . .

RUN

EXPOSE $PORT

CMD nginx -g 'daemon off;'
