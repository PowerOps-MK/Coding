# v1.23
FROM nginx@sha256:0047b729188a15da49380d9506d65959cce6d40291ccfb4e039f5dc7efd33286

WORKDIR /usr/share/nginx

COPY ./conf.d/default.conf.template /etc/nginx/conf.d/default.conf.template

COPY . .

# Required for Heroku
# CMD /bin/bash -c "envsubst '\$PORT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf" && nginx -g 'daemon off;'
