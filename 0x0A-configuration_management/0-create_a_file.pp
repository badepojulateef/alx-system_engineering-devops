# This module creates a file

$filepath = '/tmp/school'
$filemode = '0744'
$fileowner = 'www-data'
$filegroup = 'www-data'
$filecontent = 'I love Puppet\n'

# Create the file resources
file { $filepath:
  ensure  => 'file',
  mode    => $filemode,
  owner   => $fileowner,
  group   => $filegroup,
  content => $filecontenit,
}
