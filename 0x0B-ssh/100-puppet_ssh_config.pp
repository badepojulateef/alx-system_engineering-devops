# This puppet manifest makes use of puppet to
# make changes to our configuration file

exec { 'Configure file': 
  command => '/bin/echo -e "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path => '/etc/ssh/ssh_config',
}
