FROM nginx

WORKDIR /usr/share/nginx

COPY ./conf.d/default.conf.template /etc/nginx/conf.d/default.conf.template

COPY . .

EXPOSE $PORT

CMD /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx -g 'daemon off;'
