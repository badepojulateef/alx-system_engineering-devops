# This puppet manifest makes use of puppet to
# make changes to our configuration file

exec {
  command => '/bin/echo -e "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path => '/etc/ssh/ssh_config',
}
