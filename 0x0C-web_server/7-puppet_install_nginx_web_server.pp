# This puppet manifest installs and configure nginx web server

exec {'Configure ubuntu machine':
  command  => 'sudo apt-get update;
		sudo apt-get install nginx -y;
		echo "Hello World!" | sudo tee /var/www/html/index.html;
		new_config="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.blog.ehoneahobed.com permanent;"
		sudo sed -i "s/server_name _;/$new_config/" /etc/nginx/sites-enabled/default
		sudo service nginx restart',
  provider => shell,
}
