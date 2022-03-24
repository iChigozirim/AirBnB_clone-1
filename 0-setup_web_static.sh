#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt update
sudo apt install -y nginx

mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

test -L /data/web_static/current && rm /data/web_static/current || \
	ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R $USER:$USER /data/
sudo chmod -R 755 /data

print %s "server {
	listen: 80 default_server;
	listen[::]:80 default_server;

	root /etc/nginx/html;
	index index.html index.htm index.nginx-debian.html;

	location /hbnb_static {
		alias /data/web_static/current/;
		internal;
	}
}" > /etc/nginx/sites-available/default

service nginx restart
