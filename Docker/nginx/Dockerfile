FROM nginx

WORKDIR /usr/share/nginx

COPY ./conf.d/default.conf.template /etc/nginx/conf.d/default.conf.template

# COPY ./conf.d/nginx.conf /etc/nginx/nginx.conf

COPY . .

EXPOSE $PORT

RUN envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

CMD nginx -g 'daemon off;'
