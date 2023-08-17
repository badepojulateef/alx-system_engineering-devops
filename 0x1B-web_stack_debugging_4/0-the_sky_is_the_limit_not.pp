# This script increases the load of a server

exec {'increase-load':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}


# Restart Nginx
-> exec {'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
