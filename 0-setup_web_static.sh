#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

sudo chown -R ubuntu:ubuntu /data/
sudo chmod -R 755 /data/

echo "Holberton School" >> /data/web_static/releases/test/index.html

test -L /data/web_static/current && rm /data/web_static/current ; \
        sudo ln -s /data/web_static/releases/test/ /data/web_static/current

print %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;

        root /var/www/html;
        index index.html index.htm;

        location /hbnb_static {
                alias /data/web_static/current/;
                internal;
        }
}" > /etc/nginx/sites-available/default

service nginx restart
