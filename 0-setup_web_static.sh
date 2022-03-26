#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

chown -R ubuntu:ubuntu /data/
chmod -R 755 /data/

echo "Holberton School" >> /data/web_static/releases/test/index.html

#test -L /data/web_static/current && rm /data/web_static/current ; \
ln -s /data/web_static/releases/test/ /data/web_static/current

print %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;

        root /var/www/html;
        index index.html index.htm;

        location /hbnb_static {
                alias /data/web_static/current/;
                index index.html index.htm;
        }
}" > /etc/nginx/sites-available/default

service nginx restart
