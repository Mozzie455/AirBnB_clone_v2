#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

sudo apt-get update -y
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
sudo echo "im alive!" | sudo tee /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo rm -f /etc/nginx/modules-available/default
sudo cp config_file /etc/nginx/sites-available/default
sudo service nginx restart
