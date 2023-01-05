FROM nginx:1.23

WORKDIR /usr/share/nginx

COPY ./conf.d/default.conf.template /etc/nginx/conf.d/default.conf.template

COPY . .

# Required for Heroku
# CMD /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx -g 'daemon off;'
