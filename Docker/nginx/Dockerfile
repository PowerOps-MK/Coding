FROM nginx:alpine

WORKDIR /usr/share/nginx

COPY ./conf.d/default.conf.template /etc/nginx/conf.d/default.conf.template

COPY . .

RUN envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

EXPOSE $PORT

CMD nginx -g 'daemon off;'
