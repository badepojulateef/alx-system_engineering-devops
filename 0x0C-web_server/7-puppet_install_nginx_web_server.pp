# This puppet manifest installs and configure nginx web server

exec {'Configure ubuntu machine':
  command  => 'sudo apt-get update;
		sudo apt-get install nginx -y;
		echo "Hello World!" | sudo tee /var/www/html/index.html;
		sudo sed -i "server_name _;/a $new_config" /etc/nginx/sites-enabled/default;
		sudo service nginx restart',
  provider => shell,
}
